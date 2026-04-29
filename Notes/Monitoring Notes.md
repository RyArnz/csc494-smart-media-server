# Monitoring Notes

## Overview

The smart media server uses Prometheus and Grafana to monitor server and container health.

Monitoring is included so the project can show whether the server is running correctly and how system resources are being used.

---

## Monitoring Stack

The monitoring stack includes:

- Prometheus
- Grafana
- Node Exporter
- cAdvisor

---

## Prometheus

Prometheus collects and stores metrics.

It scrapes metrics from configured targets.

In this project, Prometheus targets include:

```text
Prometheus
Node Exporter
cAdvisor
```

---

## Grafana

Grafana displays Prometheus data in dashboards.

Grafana makes it easier to view system health visually.

---

## Node Exporter

Node Exporter provides host-level metrics.

Examples:

- CPU usage
- RAM usage
- Disk usage
- Filesystem data
- System load

---

## cAdvisor

cAdvisor provides Docker container metrics.

Examples:

- Container CPU usage
- Container memory usage
- Container count
- Container resource activity

---

## Why Prometheus Scrapes Itself

Prometheus scrapes its own endpoint so it can monitor its own health.

This helps verify that Prometheus is running correctly.

---

## Common Metrics to Watch

Useful metrics include:

```text
CPU usage
RAM usage
Disk usage
Container CPU usage
Container memory usage
Container count
Prometheus target status
```

---

## Example Prometheus Checks

Check Prometheus readiness:

```bash
curl http://localhost:9090/-/ready
```

Check Prometheus API:

```bash
curl "http://localhost:9090/api/v1/query?query=up"
```

---

## Example Metrics Used by the Raspberry Pi

The Raspberry Pi can use simplified metrics such as:

```text
server_cpu_percent
server_ram_percent
disk_usage_percent
```

These values can decide which LED should turn on.

---

## Monitoring Use in This Repository

Monitoring is a support feature for the smart media server.

It is not the main focus of this repository.

The main focus is the full smart media server system:

```text
Plex + Nextcloud + Docker + Cloudflare Tunnel + Nginx Proxy Manager + Raspberry Pi
```

---

## Related Machine Learning Monitoring Repository

A separate repository exists for deeper Prometheus data analysis and machine learning:

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

That repository is related, but this repository only needs enough monitoring documentation to explain how the server is observed and checked.
