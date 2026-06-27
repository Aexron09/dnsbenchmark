# DNS Benchmark

High-performance DNS benchmark for VPSs.

Measures:

- DNS lookup
- TCP connection
- TLS handshake
- Time To First Byte
- Download latency
- Reliability
- CDN selection
- Overall score

## Install

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

Run

```bash
python benchmark.py
```