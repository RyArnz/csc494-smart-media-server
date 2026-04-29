# Setup Guide

## Overview

This guide explains the general setup process for the CSC 494 Smart Media Server.

The exact commands may vary depending on the server path, Docker configuration, and domain settings.

---

## 1. Prepare the Server

The project uses Ubuntu Server as the main host.

The server should have:

- Network access
- SSH access
- Docker installed
- Docker Compose installed
- Storage for media files
- Storage for Nextcloud files
- Enough resources to run multiple containers

---

## 2. Create Project Folders

Example folder setup:

```bash
mkdir -p ~/docker
mkdir -p /data/media
mkdir -p /data/media/movies
mkdir -p /data/media/music
mkdir -p /data/media/tv
mkdir -p /data/plex/config
mkdir -p /data/nextcloud/html
mkdir -p /data/nextcloud/data
mkdir -p /data/nextcloud/db
```

---

## 3. Start Docker Services

From the repository folder, run:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

---

## 4. Configure Plex

Plex should use:

```text
/data/media -> /media
/data/plex/config -> /config
```

After the container starts, finish setup through the Plex web interface.

---

## 5. Configure Nextcloud

Nextcloud should connect to the MariaDB container.

Use the database settings from `docker-compose.yml`.

The placeholder passwords in the example file should be replaced with private values before real deployment.

---

## 6. Configure Nginx Proxy Manager

Nginx Proxy Manager should route each domain to the correct service.

Example:

```text
cloud.arnzenserver.org -> Nextcloud
media.arnzenserver.org -> Plex
```

---

## 7. Configure Cloudflare Tunnel

Cloudflare Tunnel should forward public traffic to Nginx Proxy Manager.

The simplified flow is:

```text
Cloudflare -> Cloudflare Tunnel -> localhost:80 -> Nginx Proxy Manager
```

---

## 8. Configure Prometheus

Prometheus uses:

```text
monitoring/prometheus.yml
```

The included configuration scrapes:

- Prometheus
- node_exporter
- cAdvisor

---

## 9. Configure Grafana

Grafana should use Prometheus as its data source.

Prometheus URL from inside the Docker network:

```text
http://prometheus:9090
```

---

## 10. Configure Raspberry Pi Script

Edit this line in the Raspberry Pi script:

```python
PROMETHEUS_QUERY_URL = "http://SERVER_IP:9090/api/v1/query"
```

Replace `SERVER_IP` with the actual server IP address.

Install dependencies:

```bash
pip install requests gpiozero
```

Run:

```bash
python3 scripts/raspberry_pi_status.py
```

---

## Verification Checklist

- [ ] Docker containers start
- [ ] Plex opens locally
- [ ] Nextcloud opens locally
- [ ] Cloudflare Tunnel is running
- [ ] Nginx Proxy Manager routes domains correctly
- [ ] Plex works through the media domain
- [ ] Nextcloud works through the cloud domain
- [ ] Prometheus targets are up
- [ ] Grafana dashboard loads metrics
- [ ] Raspberry Pi script can reach Prometheus
