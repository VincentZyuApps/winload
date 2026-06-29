package main

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
	"time"
)

// ========== 配置 ==========

const (
	svgWidth    = 600
	barHeight   = 28
	barPadding  = 8
	outputDir   = "../docs/benchmark"
	svgFileName = "benchmark.svg"
)

// ========== 数据结构 ==========

type HyperfineResult struct {
	Results []struct {
		Command string  `json:"command"`
		Mean    float64 `json:"mean"`   // 秒
		Stddev  float64 `json:"stddev"` // 秒
		Min     float64 `json:"min"`
		Max     float64 `json:"max"`
	} `json:"results"`
}

type OtherMetrics struct {
	BinarySize map[string]float64 `json:"binary_size"` // 字节
	MemoryRSS  map[string]float64 `json:"memory_rss"`  // KB
	CPUUsage   map[string]float64 `json:"cpu_usage"`   // % (idle)
}

type BenchmarkData struct {
	StartupTime HyperfineResult
	Metrics     OtherMetrics
	SystemInfo  string
}

// ========== 颜色配置 ==========

var toolColors = map[string]string{
	"nload (C++)":    "#f34b7d",
	"winload (Rust)": "#dea584",
	"winload (Py)":   "#3572A5",
}

// ========== SVG 生成 ==========

func generateSVG(data BenchmarkData) string {
	// 准备数据行
	// 我们需要生成 3 个图表区域：
	// 1. Startup Time (Mean) - lower is better
	// 2. Binary Size - lower is better
	// 3. Memory Usage (RSS) - lower is better

	// 提取数据
	type Item struct {
		Name  string
		Value float64
		Label string
		Color string
	}

	groups := []struct {
		Title string
		Items []Item
	}{
		{
			Title: "Startup Time (lower is better)",
			Items: []Item{},
		},
		{
			Title: "Binary Size (lower is better)",
			Items: []Item{},
		},
		{
			Title: "Memory Usage (RSS) (lower is better)",
			Items: []Item{},
		},
		{
			Title: "CPU Usage (20s @ 50ms) (lower is better)",
			Items: []Item{},
		},
	}

	// 1. Startup Time
	for _, res := range data.StartupTime.Results {
		name := parseCommandName(res.Command)
		groups[0].Items = append(groups[0].Items, Item{
			Name:  name,
			Value: res.Mean * 1000, // 转 ms
			Label: fmt.Sprintf("%.1f ms", res.Mean*1000),
			Color: toolColors[name],
		})
	}

	// 2. Binary Size
	// Sort keys to ensure consistent order if map iteration is random
	binKeys := []string{"nload (C++)", "winload (Rust)", "winload (Py)"}
	for _, name := range binKeys {
		if val, ok := data.Metrics.BinarySize[name]; ok {
			valMB := float64(val) / 1024 / 1024
			label := fmt.Sprintf("%.2f MB", valMB)
			if valMB < 0.1 {
				label = fmt.Sprintf("%.0f KB", float64(val)/1024)
			}
			groups[1].Items = append(groups[1].Items, Item{
				Name:  name,
				Value: float64(val),
				Label: label,
				Color: toolColors[name],
			})
		}
	}

	// 3. Memory
	for _, name := range binKeys {
		if val, ok := data.Metrics.MemoryRSS[name]; ok {
			label := fmt.Sprintf("%.1f MB", val/1024)
			groups[2].Items = append(groups[2].Items, Item{
				Name:  name,
				Value: val,
				Label: label,
				Color: toolColors[name],
			})
		}
	}

	// 4. CPU
	hasCPU := false
	for _, name := range binKeys {
		if val, ok := data.Metrics.CPUUsage[name]; ok {
			hasCPU = true
			label := fmt.Sprintf("%.2f%%", val)
			groups[3].Items = append(groups[3].Items, Item{
				Name:  name,
				Value: val,
				Label: label,
				Color: toolColors[name],
			})
		}
	}
	if !hasCPU {
		// remove cpu group if empty
		groups = groups[:3]
	}

	// Filter empty groups
	type Group struct {
		Title string
		Items []Item
	}
	var activeGroups []Group
	for _, g := range groups {
		if len(g.Items) > 0 {
			activeGroups = append(activeGroups, g)
		}
	}

	var sb strings.Builder

	// Parse System Info lines
	sysInfoLines := strings.Split(data.SystemInfo, "|")
	for i := range sysInfoLines {
		sysInfoLines[i] = strings.TrimSpace(sysInfoLines[i])
	}

	// Dynamic Header Height
	// Title y=40
	// Lines start y=70, step 20
	headerLineHeight := 20.0
	headerLinesStartY := 70.0

	// Separator is below last line
	separatorY := headerLinesStartY + float64(len(sysInfoLines))*headerLineHeight - 10.0
	contentStartY := separatorY + 20.0

	// Calculate total height
	// Header area + Content area + Footer area (30px)
	totalContentHeight := 0.0
	for _, g := range activeGroups {
		totalContentHeight += 50.0 + float64(len(g.Items))*(barHeight+barPadding)
	}
	totalHeight := contentStartY + totalContentHeight + 30.0

	sb.WriteString(fmt.Sprintf(`<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%.0f" viewBox="0 0 %d %.0f">
<defs>
  <style>
    .bg { fill: #0d1117; rx: 10; }
    .title { font-family: 'Segoe UI', sans-serif; font-size: 18px; font-weight: 600; fill: #58a6ff; }
    .subtitle { font-family: 'Segoe UI', sans-serif; font-size: 12px; fill: #8b949e; }
    .group-title { font-family: 'Segoe UI', sans-serif; font-size: 14px; font-weight: 600; fill: #c9d1d9; }
    .label { font-family: 'Segoe UI', sans-serif; font-size: 12px; fill: #e6edf3; }
    .value { font-family: 'Segoe UI', sans-serif; font-size: 12px; fill: #8b949e; }
    .bar-bg { fill: #161b22; rx: 4; }
    .row { opacity: 0; animation: fadeInRight 0.8s ease forwards; }
    @keyframes fadeInRight { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: translateX(0); } }
  </style>
</defs>
<rect class="bg" width="100%%" height="100%%"/>
`, svgWidth, totalHeight, svgWidth, totalHeight))

	// Main Title
	sb.WriteString(`<text class="title" x="30" y="40">⚡ Winload Benchmarks</text>`)

	// System Info Lines
	for i, line := range sysInfoLines {
		y := headerLinesStartY + float64(i)*headerLineHeight
		sb.WriteString(fmt.Sprintf(`<text class="subtitle" x="30" y="%.0f">%s</text>
`, y, line))
	}

	// Separator
	sb.WriteString(fmt.Sprintf(`<line x1="30" y1="%.0f" x2="%d" y2="%.0f" stroke="#30363d" stroke-width="1"/>
`, separatorY, svgWidth-30, separatorY))

	currentY := contentStartY

	for gIdx, group := range activeGroups {
		// Group Title
		sb.WriteString(fmt.Sprintf(`<text class="group-title" x="30" y="%.0f">%s</text>
`, currentY+15, group.Title))

		currentY += 30

		// Find max value for scaling column
		maxVal := 0.0
		for _, it := range group.Items {
			if it.Value > maxVal {
				maxVal = it.Value
			}
		}
		if maxVal == 0 {
			maxVal = 1
		}

		for i, item := range group.Items {
			barW := 300.0 // max width of bar
			w := (item.Value / maxVal) * barW
			if w < 2 {
				w = 2
			} // min width

			// delay relative to previous items (~10s total playback)
			delay := float64(gIdx)*2.5 + float64(i)*0.6
			y := currentY + float64(i)*(barHeight+barPadding)

			sb.WriteString(fmt.Sprintf(`<g class="row" style="animation-delay: %.1fs">
`, delay))

			// Name
			sb.WriteString(fmt.Sprintf(`<text class="label" x="30" y="%.0f">%s</text>
`, y+20, item.Name))

			// Bar BG
			sb.WriteString(fmt.Sprintf(`<rect class="bar-bg" x="140" y="%.0f" width="%.0f" height="20"/>
`, y+6, barW))

			// Bar Fill
			sb.WriteString(fmt.Sprintf(`<rect x="140" y="%.0f" width="%.0f" height="20" rx="3" fill="%s">
  <animate attributeName="width" from="0" to="%.0f" dur="1.5s" begin="%.1fs" fill="freeze"/>
</rect>
`, y+6, w, item.Color, w, delay))

			// Value Label
			sb.WriteString(fmt.Sprintf(`<text class="value" x="%.0f" y="%.0f">%s</text>
`, 140.0+barW+10, y+20, item.Label))

			sb.WriteString(`</g>
`)
		}
		currentY += float64(len(group.Items))*(barHeight+barPadding) + 20
	}

	// Footer
	sb.WriteString(fmt.Sprintf(`<text class="subtitle" x="30" y="%.0f">📅 Updated: %s</text>
</svg>`, totalHeight-15, time.Now().Format("2006-01-02 15:04:05")))

	return sb.String()
}

func parseCommandName(cmd string) string {
	if strings.Contains(cmd, "nload") && !strings.Contains(cmd, "winload") {
		return "nload (C++)"
	}
	// Rust binary is invoked via explicit path: ./rust/.../winload
	// Python binary is a bare "winload" installed into venv PATH
	if strings.Contains(cmd, "winload") {
		if strings.Contains(cmd, "rust/") || strings.Contains(cmd, "target/release") {
			return "winload (Rust)"
		}
		// Explicit python markers
		if strings.Contains(cmd, ".py") || strings.Contains(cmd, "python") || strings.Contains(cmd, "pip") || strings.Contains(cmd, "import") {
			return "winload (Py)"
		}
		// Bare "winload" without path = Python (installed via uv pip)
		if !strings.Contains(cmd, "/") && !strings.Contains(cmd, "\\") {
			return "winload (Py)"
		}
		// Fallback: unknown winload variant
		return "winload (Rust)"
	}
	return cmd
}

// ========== Main ==========

func main() {
	// 读取 hyperfine json
	startJSON, err := os.ReadFile("startup_time.json")
	var bench HyperfineResult
	if err == nil {
		if err := json.Unmarshal(startJSON, &bench); err != nil {
			log.Printf("Error unmarshalling startup_time.json: %v", err)
		}
	} else {
		log.Println("Warning: startup_time.json not found, skipping startup section")
	}

	// 读取其他指标 (通过环境变量或简单文件传入，这里假设 CI 脚本输出了 metrics.json)
	metricsJSON, err := os.ReadFile("metrics.json")
	var metrics OtherMetrics
	if err == nil {
		if err := json.Unmarshal(metricsJSON, &metrics); err != nil {
			log.Printf("Error unmarshalling metrics.json: %v", err)
		}
	} else {
		log.Println("Warning: metrics.json not found, skipping metrics section")
	}

	// 获取系统信息
	sysInfo := os.Getenv("BENCHMARK_SYS_INFO")
	if sysInfo == "" {
		sysInfo = "Running on GitHub Actions"
	}

	data := BenchmarkData{
		StartupTime: bench,
		Metrics:     metrics,
		SystemInfo:  sysInfo,
	}

	svg := generateSVG(data)

	if err := os.MkdirAll(outputDir, 0755); err != nil {
		log.Fatal(err)
	}

	absPath, _ := filepath.Abs(filepath.Join(outputDir, svgFileName))
	err = os.WriteFile(absPath, []byte(svg), 0644)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("✅ Benchmark SVG generated at: %s\n", absPath)
}
