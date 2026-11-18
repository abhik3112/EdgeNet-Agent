import time
from typing import cast
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from telemetry import NetworkTelemetrySimulator
from tools import GatewayTools
from profiler import EdgeProfilerEngine

console = Console()

class EdgeNetAgent:
    def __init__(self):
        self.telemetry = NetworkTelemetrySimulator()
        self.profiler = EdgeProfilerEngine()
        console.print(Panel.fit("[bold cyan]EdgeNet-Agent[/bold cyan] | Edge Gateway AI Telemetry & Diagnostic Runtime", border_style="cyan"))

    def run_diagnostic_cycle(self, cycle_num):
        # 1. Ingest telemetry & run profiled inference
        data = self.telemetry.simulate_gateway_telemetry()
        profile_result = self.profiler.run_quantized_inference_simulation()
        metrics = cast(dict[str, float], profile_result["edge_profile_metrics"])
        
        # 2. Evaluate health
        health_check = GatewayTools.check_connection_health(
            data["ping_latency_ms"], 
            data["packet_loss_percent"]
        )
        is_degraded = data["anomaly_detected"] or health_check["status"] == "DEGRADED"
        status_color = "bold red" if is_degraded else "bold green"

        # 3. Build Visual Telemetry Table
        table = Table(title=f"Diagnostic Cycle #{cycle_num} [{data['timestamp']}]", show_header=True, header_style="bold magenta")
        table.add_column("Metric / Component", style="dim", width=28)
        table.add_column("Measured Value", width=25)
        table.add_column("Edge Threshold / Target", width=25)

        table.add_row("Ping Latency", f"{data['ping_latency_ms']} ms", "< 70.0 ms")
        table.add_row("Packet Loss", f"{data['packet_loss_percent']} %", "< 3.0 %")
        table.add_row("Wi-Fi Signal (RSSI)", f"{data['wi_fi_rssi_dbm']} dBm", "> -65 dBm")
        table.add_row("NPU Inference Latency", f"[cyan]{metrics['latency_ms']} ms[/cyan]", "< 25.0 ms (Real-time)")
        table.add_row("Process Memory Delta", f"{metrics['memory_delta_mb']} MB", "< 5.0 MB Overhead")
        table.add_row("Agent Health Assessment", f"[{status_color}]{health_check['status']}[/{status_color}]", health_check['reason'])

        console.print(table)

        # 4. Trigger Tool-Calling if needed
        if is_degraded:
            console.print("[bold yellow]⚡ Anomaly Detected -> Invoking Agentic Remediation Tools...[/bold yellow]")
            ping_res = GatewayTools.run_diagnostic_ping()
            rem_res = GatewayTools.optimize_channel_or_reset_socket()
            console.print(f"   [green]✔[/green] [bold]run_diagnostic_ping()[/bold]: {ping_res['output']}")
            console.print(f"   [green]✔[/green] [bold]optimize_channel_or_reset_socket()[/bold]: {rem_res['action_taken']} -> [bold green]{rem_res['status']}[/bold green]\n")
        else:
            console.print("[green]✔ System Nominal. No tool intervention required.[/green]\n")

if __name__ == "__main__":
    agent = EdgeNetAgent()
    for i in range(1, 3):
        agent.run_diagnostic_cycle(i)
        time.sleep(1.0)