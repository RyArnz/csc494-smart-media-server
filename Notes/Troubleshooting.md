# Troubleshooting

## Overview

This file documents common problems and fixes for the smart media server project.

---

## Plex Works Locally but Not Remotely

### Cause

The remote traffic path may not be correct.

The required path is:

```text
Cloudflare -> Cloudflare Tunnel -> Nginx Proxy Manager -> Plex
```

### Fix

Check:

- Cloudflare DNS record
- Cloudflare Tunnel status
- Nginx Proxy Manager proxy host
- Plex container status
- Correct internal Plex port

---

## Media Domain Shows Wrong Page

### Cause

The domain is reaching the server, but Nginx Proxy Manager is routing it incorrectly.

### Fix

Check the Nginx Proxy Manager proxy host for:

- Correct domain name
- Correct forward hostname
- Correct forward port
- Correct scheme
- WebSocket support if needed

---

## Grafana Opens but Shows No Data

### Cause

Grafana may not be connected to Prometheus, or Prometheus may not have working scrape targets.

### Fix

Check Prometheus targets:

```text
http://SERVER_IP:9090/targets
```

Check Prometheus readiness:

```bash
curl http://SERVER_IP:9090/-/ready
```

Check Grafana data source:

```text
http://prometheus:9090
```

---

## Prometheus Target Is Down

### Cause

A target may be down because the container is stopped, the target name is wrong, or the port is incorrect.

### Fix

Check containers:

```bash
docker ps
```

Check logs:

```bash
docker logs prometheus
docker logs node-exporter
docker logs cadvisor
```

---

## Docker Compose Fails

### Cause

Possible causes include:

- YAML indentation error
- Missing folder
- Port conflict
- Missing environment value
- Permission problem

### Fix

Validate compose file:

```bash
docker compose config
```

Start services:

```bash
docker compose up -d
```

View logs:

```bash
docker compose logs
```

---

## Raspberry Pi Cannot Reach Prometheus

### Cause

Possible causes include:

- Wrong server IP
- Prometheus not running
- Network issue
- Firewall issue
- Wrong port

### Fix

From the Raspberry Pi:

```bash
ping SERVER_IP
curl http://SERVER_IP:9090/-/ready
```

Then update:

```python
PROMETHEUS_QUERY_URL = "http://SERVER_IP:9090/api/v1/query"
```

---

## General Debugging Order

Use this order:

1. Check power and network
2. Check Docker
3. Check containers
4. Check logs
5. Check local service access
6. Check Nginx Proxy Manager
7. Check Cloudflare Tunnel
8. Check DNS
9. Check remote access
10. Check monitoring dashboards
