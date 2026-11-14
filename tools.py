import subprocess
import platform

class GatewayTools:
    @staticmethod
    def check_connection_health(latency, packet_loss):
        """Analyzes core connection metrics and returns diagnostic status."""
        if packet_loss > 3.0 or latency > 70.0:
            return {"status": "DEGRADED", "reason": f"High latency ({latency}ms) or packet loss ({packet_loss}%)."}
        return {"status": "OPTIMAL", "reason": "Connection parameters are within normal thresholds."}

    @staticmethod
    def run_diagnostic_ping(host="8.8.8.8", count=2):
        """Executes a real system ping to check gateway reachability."""
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, str(count), host]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=3)
            if result.returncode == 0:
                return {"tool": "run_diagnostic_ping", "success": True, "output": "Target reachable."}
            else:
                return {"tool": "run_diagnostic_ping", "success": False, "output": "Target unreachable or packet dropped."}
        except Exception as e:
            return {"tool": "run_diagnostic_ping", "success": False, "error": str(e)}

    @staticmethod
    def optimize_channel_or_reset_socket():
        """Simulates executing an edge corrective action (e.g., channel switch or socket flush)."""
        # In a real edge deployment, this would interface with router APIs / hostapd / netsh
        return {
            "tool": "optimize_channel_or_reset_socket",
            "action_taken": "Flushed socket buffers and shifted Wi-Fi channel to reduce interference.",
            "status": "RESOLVED"
        }