import time
from telemetry import NetworkTelemetrySimulator
from tools import GatewayTools
from profiler import EdgeProfilerEngine

class EdgeNetAgent:
    def __init__(self):
        self.telemetry = NetworkTelemetrySimulator()
        self.profiler = EdgeProfilerEngine()
        print("[EdgeNet-Agent] Initialized with Edge Profiling & Telemetry Modules.")

    def run_diagnostic_cycle(self):
        print("\n" + "="*50)
        print("--- Starting Edge Diagnostic & Profiling Cycle ---")
        
        # 1. Ingest telemetry data
        data = self.telemetry.simulate_gateway_telemetry()
        print(f"[{data['timestamp']}] Telemetry -> Ping: {data['ping_latency_ms']}ms | Packet Loss: {data['packet_loss_percent']}% | RSSI: {data['wi_fi_rssi_dbm']} dBm")

        # 2. Run profiled edge model inference simulation
        profile_result = self.profiler.run_quantized_inference_simulation()
        metrics = profile_result["edge_profile_metrics"]
        print(f"Edge Runtime Profile [{profile_result['model']}]:")
        print(f"  -> Latency: {metrics['latency_ms']} ms | Memory Delta: {metrics['memory_delta_mb']} MB")

        # 3. Evaluate health via tool logic
        health_check = GatewayTools.check_connection_health(
            data["ping_latency_ms"], 
            data["packet_loss_percent"]
        )
        print(f"Agent Health Assessment: {health_check['status']} ({health_check['reason']})")

        # 4. Trigger tool action if anomalous
        if data["anomaly_detected"] or health_check["status"] == "DEGRADED":
            print("[Agent Action Triggered] Anomaly or degradation identified. Executing remediation tools...")
            ping_result = GatewayTools.run_diagnostic_ping()
            print(f"  -> Tool Result: {ping_result['output']}")

            remediation = GatewayTools.optimize_channel_or_reset_socket()
            print(f"  -> Tool Action: {remediation['action_taken']} [{remediation['status']}]")
        else:
            print("[Agent Status] All systems nominal. Edge routine executed efficiently.")

if __name__ == "__main__":
    agent = EdgeNetAgent()
    # Run 2 demonstration cycles
    for i in range(2):
        agent.run_diagnostic_cycle()
        time.sleep(1.0)