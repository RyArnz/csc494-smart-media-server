import time
import requests

try:
    from gpiozero import LED
except ImportError:
    LED = None


PROMETHEUS_QUERY_URL = "http://SERVER_IP:9090/api/v1/query"

GREEN_PIN = 17
BLUE_PIN = 27
YELLOW_PIN = 19
RED_PIN = 26

CPU_WARN = 70.0
RAM_WARN = 80.0
DISK_CRIT = 90.0

REFRESH_SECONDS = 15

CPU_QUERY = '100 - (avg(rate(node_cpu_seconds_total{job="node_exporter",mode="idle"}[1m])) * 100)'
RAM_QUERY = '100 * (1 - (node_memory_MemAvailable_bytes{job="node_exporter"} / node_memory_MemTotal_bytes{job="node_exporter"}))'
DISK_QUERY = '100 * (1 - (max by(instance) (node_filesystem_avail_bytes{job="node_exporter",fstype!~"tmpfs|overlay",mountpoint="/"}) / max by(instance) (node_filesystem_size_bytes{job="node_exporter",fstype!~"tmpfs|overlay",mountpoint="/"})))'


def prom_query(query: str) -> float:
    response = requests.get(
        PROMETHEUS_QUERY_URL,
        params={"query": query},
        timeout=5,
    )
    response.raise_for_status()

    data = response.json()
    results = data.get("data", {}).get("result", [])

    if not results:
        raise ValueError("Prometheus returned no result for query.")

    value = results[0]["value"][1]
    return float(value)


class StatusLights:
    def __init__(self):
        if LED is None:
            self.enabled = False
            self.green = None
            self.blue = None
            self.yellow = None
            self.red = None
            print("gpiozero is not installed. Running in console-only mode.")
        else:
            self.enabled = True
            self.green = LED(GREEN_PIN)
            self.blue = LED(BLUE_PIN)
            self.yellow = LED(YELLOW_PIN)
            self.red = LED(RED_PIN)

    def all_off(self):
        if not self.enabled:
            return

        self.green.off()
        self.blue.off()
        self.yellow.off()
        self.red.off()

    def set_status(self, status: str):
        self.all_off()

        if status == "healthy":
            print("STATUS: HEALTHY")
            if self.enabled:
                self.green.on()

        elif status == "warning":
            print("STATUS: WARNING")
            if self.enabled:
                self.yellow.on()

        elif status == "critical":
            print("STATUS: CRITICAL")
            if self.enabled:
                self.red.on()

        else:
            print("STATUS: CONNECTION ERROR")
            if self.enabled:
                self.blue.on()


def get_server_status() -> str:
    cpu = prom_query(CPU_QUERY)
    ram = prom_query(RAM_QUERY)
    disk = prom_query(DISK_QUERY)

    print(f"CPU:  {cpu:.2f}%")
    print(f"RAM:  {ram:.2f}%")
    print(f"DISK: {disk:.2f}%")

    if disk >= DISK_CRIT:
        return "critical"

    if cpu >= CPU_WARN or ram >= RAM_WARN:
        return "warning"

    return "healthy"


def main():
    lights = StatusLights()

    while True:
        try:
            status = get_server_status()
            lights.set_status(status)

        except Exception as error:
            print(f"Error checking server status: {error}")
            lights.set_status("connection_error")

        print("-" * 40)
        time.sleep(REFRESH_SECONDS)


if __name__ == "__main__":
    main()
