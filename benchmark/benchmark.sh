#!/bin/bash
set -e

# =========================================================================================
# Winload Benchmark Script
# run this in linux, for example: WSL Debian13
# =========================================================================================
# Need sudo permissions for installing dependencies.
# Usage: ./benchmark.sh [--proxy http://xxx:port]
# E.g.:  `chmod +x ./benchmark.sh`
# Then: `./benchmark.sh --proxy http://192.168.31.233:7890`
# =========================================================================================

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 0. Environment Setup
# Get the absolute path to the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Go to project root (parent directory of benchmark)
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

# Parse arguments
PROXY_URL=""
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --proxy) PROXY_URL="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [ ! -z "$PROXY_URL" ]; then
    echo -e "${YELLOW}🌐 Setting proxy to $PROXY_URL${NC}"
    export http_proxy="$PROXY_URL"
    export https_proxy="$PROXY_URL"
    export HTTP_PROXY="$PROXY_URL"
    export HTTPS_PROXY="$PROXY_URL"
fi


echo -e "${GREEN}🚀 Starting Winload Benchmark...${NC}"
echo "Project Root: $PROJECT_ROOT"

# 1. Check & Install Dependencies
echo -e "${YELLOW}📦 Checking dependencies...${NC}"

if ! command -v cargo &> /dev/null; then
    echo -e "${RED}Error: Rust (cargo) is not installed.${NC}"
    exit 1
fi

if ! command -v go &> /dev/null; then
    echo -e "${RED}Error: Go is not installed.${NC}"
    exit 1
fi

if ! command -v uv &> /dev/null; then
    echo -e "${YELLOW}uv not found. Installing uv...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

if ! uv python find 3.13 &> /dev/null; then
    echo -e "${YELLOW}Python 3.13 is not available to uv. Installing it...${NC}"
    if ! uv python install 3.13; then
        echo -e "${RED}Error: Failed to install Python 3.13 with uv.${NC}"
        exit 1
    fi
fi

TOOLS_TO_INSTALL=""
if ! command -v hyperfine &> /dev/null; then
    TOOLS_TO_INSTALL="$TOOLS_TO_INSTALL hyperfine"
fi
if ! command -v nload &> /dev/null; then
    TOOLS_TO_INSTALL="$TOOLS_TO_INSTALL nload"
fi
if [ ! -f /usr/bin/time ]; then
    TOOLS_TO_INSTALL="$TOOLS_TO_INSTALL time"
fi

if [ ! -z "$TOOLS_TO_INSTALL" ]; then
    echo -e "${YELLOW}Installing missing tools: $TOOLS_TO_INSTALL (requires sudo)${NC}"
    # Use -E to preserve environment variables (proxy settings)
    sudo -E apt-get update && sudo -E apt-get install -y $TOOLS_TO_INSTALL
fi

# 2. Build Rust Binary
echo -e "${YELLOW}🔨 Building Rust release binary...${NC}"
cd rust
cargo build --release
RUST_BIN="./target/release/winload"
cd ..

if [ ! -f "rust/$RUST_BIN" ]; then
    echo -e "${RED}Error: Rust binary build failed.${NC}"
    exit 1
fi

# 3. Setup Python Environment
echo -e "${YELLOW}🐍 Setting up Python environment with uv...${NC}"

# Create venv and install
# Remove existing venv to avoid interactive prompt
rm -rf venv_bench
uv venv --python 3.13 venv_bench
source venv_bench/bin/activate
python --version

# Install from python/ directory
# We need to copy README.md to python/ directory because hatchling expects it to be next to pyproject.toml
# Also need to check if we are in case-sensitive FS.
# The previous fail was: OSError: Readme file does not exist: readme.md
# So we need to copy to 'readme.md' or make sure it matches.
# The repo file is 'readme.md' (lowercase) or 'README.md'?
# Checking file list it seems to be 'readme.md' mostly.
# Copy the package README used by python/pyproject.toml.
cp -f readme.md python/ 2>/dev/null || true
cp -f README.md python/ 2>/dev/null || true

uv pip install ./python
PY_CMD="winload"

# 4. Run Benchmarks (Hyperfine)
echo -e "${YELLOW}⏱️  Running startup time benchmarks with Hyperfine...${NC}"

# Ensure output directory exists (relative to PROJECT_ROOT)
mkdir -p benchmark

# All three use --help consistently for fair startup time comparison.
# --help measures: binary load → runtime init → arg parse → print → exit.
# This captures the real runtime overhead (e.g. Python module imports vs native code).
# -N (--shell=none) skips shell startup for more accurate sub-10ms measurements.

hyperfine --warmup 3 --min-runs 10 -N --export-json benchmark/startup_time.json \
    "nload --help" \
    "./rust/$RUST_BIN --help" \
    "$PY_CMD --help"

# 5. Collect Metrics
echo -e "${YELLOW}📊 Collecting binary size and memory metrics...${NC}"

# Sizes
RUST_SIZE=$(stat -c%s "rust/$RUST_BIN")
NLOAD_PATH=$(which nload)
NLOAD_SIZE=$(stat -c%s "$NLOAD_PATH")
# Collection function for uv venv size (approximate)
# Just measure the site-packages
PY_SIZE=$(du -sb venv_bench/lib/*/site-packages | cut -f1 | head -n1)

# Memory (RSS) - Using /usr/bin/time -v
# We take the "Maximum resident set size (kbytes)"
get_mem_rss() {
    cmd=$1
    # Check if /usr/bin/time exists, usually part of 'time' package
    if [ ! -f /usr/bin/time ]; then
        echo "0"
        return
    fi
    /usr/bin/time -v bash -c "$cmd" 2>&1 | grep "Maximum resident set size" | awk '{print $6}' | head -n1
}

get_cpu_usage() {
    cmd=$1
    if [ ! -f /usr/bin/time ]; then echo "0"; return; fi
    # Run with timeout to measure idle cpu over 20s
    # Use custom format -f: "%U(user) %S(sys) %e(elapsed)"
    # We capture stderr because that's where time writes its output
    
    output=$( { /usr/bin/time -f "%U %S %e" timeout 20s bash -c "$cmd" >/dev/null; } 2>&1 )
    
    # Extract the last line which should contain our numbers
    stats=$(echo "$output" | tail -n1)
    
    # Calculate: (User + System) / Elapsed * 100
    # Use %.2f for 2 decimal precision
    val=$(echo "$stats" | awk '{if ($3 > 0) printf "%.2f", ($1 + $2) / $3 * 100; else print "0.00"}')
    
    if [ -z "$val" ]; then echo "0.00"; else echo "$val"; fi
}

# Note: nload --help might be too fast to measure significant memory, but it's a baseline.
NLOAD_MEM=$(get_mem_rss "nload --help")
if [ -z "$NLOAD_MEM" ]; then NLOAD_MEM=0; fi

RUST_MEM=$(get_mem_rss "./rust/$RUST_BIN --version")
if [ -z "$RUST_MEM" ]; then RUST_MEM=0; fi

# For Python, we run module to ensure imports are loaded
PY_MEM=$(get_mem_rss "$PY_CMD --version")
if [ -z "$PY_MEM" ]; then PY_MEM=0; fi

echo -e "${YELLOW}📊 Collecting CPU usage (20s @ 50ms interval)...${NC}"
NLOAD_CPU=$(get_cpu_usage "nload -t 50")
RUST_CPU=$(get_cpu_usage "./rust/$RUST_BIN -t 50")
PY_CPU=$(get_cpu_usage "$PY_CMD -t 50")

echo "  - nload size: $(($NLOAD_SIZE/1024)) KB, mem: ${NLOAD_MEM} KB, cpu: ${NLOAD_CPU}%"
echo "  - Rust size:  $(($RUST_SIZE/1024)) KB, mem: ${RUST_MEM} KB, cpu: ${RUST_CPU}%"
echo "  - Py size:    $(($PY_SIZE/1024)) KB, mem: ${PY_MEM} KB, cpu: ${PY_CPU}%"

# Write metrics.json
cat <<EOF > benchmark/metrics.json
{
  "binary_size": {
    "nload (C++)": $NLOAD_SIZE,
    "winload (Rust)": $RUST_SIZE,
    "winload (Py)": $PY_SIZE
  },
  "memory_rss": {
    "nload (C++)": $NLOAD_MEM,
    "winload (Rust)": $RUST_MEM,
    "winload (Py)": $PY_MEM
  },
  "cpu_usage": {
    "nload (C++)": $NLOAD_CPU,
    "winload (Rust)": $RUST_CPU,
    "winload (Py)": $PY_CPU
  }
}
EOF

# Clean up copied readmes in python/ to avoid dirty git status.
# Keep python/readme.md because it is the tracked local-development placeholder.
rm -f python/README.md

# 6. Generate SVG
echo -e "${YELLOW}🎨 Generating SVG...${NC}"
# Use generic system info if empty
if [ -z "$BENCHMARK_SYS_INFO" ]; then
    # Try to detect memory
    MEM_INFO="Unknown"
    if [ -f /proc/meminfo ]; then
        # Linux
        MEM_KB=$(grep MemTotal /proc/meminfo | awk '{print $2}')
        if [ ! -z "$MEM_KB" ]; then
            MEM_INFO=$(awk "BEGIN {printf \"%.1f GB\", $MEM_KB/1024/1024}")
        fi
    elif command -v sysctl &> /dev/null; then
        # macOS
        MEM_BYTES=$(sysctl -n hw.memsize 2>/dev/null)
        if [ ! -z "$MEM_BYTES" ]; then
             MEM_INFO=$(awk "BEGIN {printf \"%.1f GB\", $MEM_BYTES/1024/1024/1024}")
        fi
    fi

    # Try to detect CPU
    CPU_INFO=""
    if [ -f /proc/cpuinfo ]; then
        CPU_INFO=$(grep -m1 'model name' /proc/cpuinfo | cut -d: -f2 | xargs)
    fi
    if [ -z "$CPU_INFO" ] && command -v sysctl &> /dev/null; then
        CPU_INFO=$(sysctl -n machdep.cpu.brand_string 2>/dev/null)
    fi
    if [ -z "$CPU_INFO" ]; then
        CPU_INFO="Unknown CPU"
    fi
    
    export BENCHMARK_SYS_INFO="Runner: $(uname -n) | OS: $(uname -s) $(uname -r) | CPU: ${CPU_INFO} | RAM: ${MEM_INFO}"
fi

cd benchmark
go run main.go
cd ..

echo -e "${GREEN}✅ Done! Check docs/benchmark/benchmark.svg${NC}"
