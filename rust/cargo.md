```shell

wsl
cargo clean
cargo check

export HOST_IP=$(ip route show default | awk '{print $3}')
export HTTPS_PROXY=http://$HOST_IP:7890
export HTTP_PROXY=http://$HOST_IP:7890
python3 build.py

python3 build.py --clean

cargo run --release -- --help

```