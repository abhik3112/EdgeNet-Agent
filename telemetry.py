import time
import random
import psutil

class NetworkTelemetrySimulator:
    def __init__(self, target_host="8.8.8.8"):
        self.target_host = target_host

    def get_system_metrics(self):
        """Gathers local system resource utilization (CPU, Memory)."""
        cpu_usage = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        return {
            "cpu_usage_percent": cpu_usage,
            "memory_usage_percent": memory.percent,
            "available_memory_mb": round(memory.available / (1024 * 1024), 2)
        }

    def simulate_gateway_telemetry(self):
        """Simulates gateway / router telemetry data streams."""
        # Simulated metrics for a residential/edge gateway device
        simulated_latency_ms = round(random.uniform(12.5, 85.0), 2)
        packet_loss_percent = round(random.choice([0.0, 0.0, 0.5, 2.1, 5.4]), 2)
        signal_strength_dbm = random.randint(-68, -42) # Wi-Fi RSSI
        
        # Introduce a sporadic network spike condition for testing anomaly detection
        is_anomaly = simulated_latency_ms > 70.0 or packet_loss_percent > 3.0

        return {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "ping_latency_ms": simulated_latency_ms,
            "packet_loss_percent": packet_loss_percent,
            "wi_fi_rssi_dbm": signal_strength_dbm,
            "anomaly_detected": is_anomaly,
            "system_health": self.get_system_metrics()
        }

if __name__ == "__main__":
    monitor = NetworkTelemetrySimulator()
    print("Initializing Edge Gateway Telemetry Stream...")
    for _ in range(3):
        print(monitor.simulate_gateway_telemetry())
        time.sleep(1)