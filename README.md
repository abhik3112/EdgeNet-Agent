# EdgeNet-Agent: Lightweight Edge Network Diagnostic & Agentic Telemetry Engine

`EdgeNet-Agent` is a Python-based edge AI and telemetry monitoring prototype designed for resource-constrained gateway devices. The system continuously ingests network telemetry, executes on-device quantized model profiling, evaluates system health, and invokes agentic tool-calling workflows to remediate network anomalies in real time.

---

## Architecture & Core Modules

The project is structured into modular, production-ready components mirroring edge software design principles:

1. **`telemetry.py` (Telemetry Ingestion Engine):** Simulates and monitors real-time gateway metrics including ping latency, packet loss, Wi-Fi RSSI (dBm), and local system resource utilization (`psutil`).
2. **`profiler.py` (Edge Performance Profiler):** Features a decorator-based benchmarking engine that measures execution latency (ms) and memory footprint deltas (MB) during quantized model inference passes (simulating MobileNetV3-Small / NPU runtimes).
3. **`tools.py` (Agentic Tool-Calling Layer):** Implements automated system actions—such as target connectivity checks, subprocess pings, and socket buffer/Wi-Fi channel optimization—invoked conditionally by the agent.
4. **`main.py` (The Agent Decision Loop):** Orchestrates the continuous monitoring cycle, evaluating health thresholds and triggering automated remediation workflows.

---

## Example Execution Output

```text
[EdgeNet-Agent] Initialized with Edge Profiling & Telemetry Modules.

==================================================
--- Starting Edge Diagnostic & Profiling Cycle ---
[2026-11-13 21:41:17] Telemetry -> Ping: 81.4ms | Packet Loss: 2.1% | RSSI: -68 dBm
Edge Runtime Profile [MobileNetV3-Gateway-Quantized]:
  -> Latency: 18.774 ms | Memory Delta: 0.0 MB
Agent Health Assessment: DEGRADED (High latency (81.4ms) or packet loss (2.1%).)
[Agent Action Triggered] Anomaly or degradation identified. Executing remediation tools...
  -> Tool Result: Target reachable.
  -> Tool Action: Flushed socket buffers and shifted Wi-Fi channel to reduce interference. [RESOLVED]