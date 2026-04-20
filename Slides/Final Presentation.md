
# Smart Home Media Server

Ryan Arnzen

---

## Project Summary

- Built a self-hosted home server on Ubuntu Server
- Centralized media streaming, cloud storage, and monitoring
- Used Docker to deploy and manage services
- Added Raspberry Pi integration for physical status indicators
- Designed the system to be expandable for automation and future smart-home features

---

## Problem

Many families rely on multiple separate platforms for:

- media streaming
- file storage
- remote access

### Problems

- repeat payments
- reduced privacy and control of data
- limited customization

---

## Solution

My solution was to build a Docker-based smart home media platform with:

- Plex for local and remote media access
- Nextcloud for personal cloud storage
- Nginx Proxy Manager for reverse-proxy/domain access for both public-facing services
- Cloudflare Tunnel for domain-based external routing
- Prometheus + Grafana for monitoring
- node_exporter + cAdvisor for host and container metrics
- Raspberry Pi 4 for system status output

---

## Architecture

### Internet

- `cloud.arnzenserver.org` → Cloudflare Tunnel → Nginx Proxy Manager → Nextcloud
- `media.arnzenserver.org` → Cloudflare Tunnel → Nginx Proxy Manager → Plex

### Ubuntu Server

- Plex
- Nextcloud
- Nginx Proxy Manager
- Cloudflared Tunnel
- Prometheus
- Grafana
- node_exporter
- cAdvisor

### Raspberry Pi 4

- Python LED status script
- Physical server-health indicators

<!-- Optional: insert architecture screenshot from original PDF page 5 -->

---

## Technology Stack

- Ubuntu Server
- Docker / Docker Compose
- Plex
- Nextcloud
- Nginx Proxy Manager
- Prometheus
- Grafana
- node_exporter
- cAdvisor
- Raspberry Pi 4
- Python 3
- gpiozero

---

## What Works

- Plex local access works
- Plex external access works through `media.arnzenserver.org`
- Nextcloud access works through `cloud.arnzenserver.org`
- Cloudflare Tunnel routing is working
- Nginx Proxy Manager routing is working
- Prometheus is collecting metrics
- Grafana dashboards are working
- Host and container monitoring are verified
- Raspberry Pi LED hardware wiring is working and ready for demo

---
<img width="1332" height="793" alt="Plex Dashboard" src="https://github.com/user-attachments/assets/b3f63777-ffb2-490e-a0d8-ee9fceebec4c" />
<img width="1440" height="900" alt="Nextcloud Dashboard" src="https://github.com/user-attachments/assets/4ce3ff2b-3f04-43b7-b109-e2fd6ff121e2" />

---

## Domain and Service Access

- Public domain routing is configured through Cloudflare
- External access is forwarded through Cloudflare Tunnel
- Nginx Proxy Manager routes traffic to internal services
- Plex and Nextcloud are both reachable through their own subdomains

<img width="1332" height="793" alt="Cloudflare DNS Management" src="https://github.com/user-attachments/assets/56bfc4d0-bd83-49db-9296-b1bc77dc280b" />

---

## Monitoring

### Monitoring services

- Prometheus for metrics collection
- Grafana for dashboards
- node_exporter for host metrics
- cAdvisor for container metrics

### What is monitored

- CPU usage
- RAM usage
- disk usage
- uptime
- container memory
- container CPU
- container count

---

## Prometheus Verification

- Prometheus targets are up
- cAdvisor is being scraped
- node_exporter is being scraped
- Prometheus is scraping its own metrics
- Monitoring pipeline is functioning correctly

<img width="1332" height="793" alt="Prometheus Endpoints" src="https://github.com/user-attachments/assets/53b40745-dad1-485a-8227-01c64cb84d96" />

---

## Grafana Results

### Node Exporter dashboard shows

- disk usage
- root filesystem usage
- uptime
- total root filesystem size

### Container dashboard shows

- total memory usage
- container count
- per-container CPU usage
- per-container memory usage
- Plex CPU and memory
- Nextcloud CPU and memory

<img width="1332" height="793" alt="Grafana Dashboard" src="https://github.com/user-attachments/assets/68e8ea1c-0269-4ba8-b76c-986cbd465511" />

---

## Raspberry Pi

### Current design

- Pi polls health and monitoring data
- Python script controls LEDs
- LEDs represent server conditions

### LED mapping

- Green = server reachable
- Blue = Plex service healthy
- Yellow = resource warning
- Red = critical issue / disk or service problem

---

## LED Hardware Setup

### Wired outputs

- GPIO17 → Green
- GPIO27 → Blue
- GPIO19 → Yellow
- GPIO26 → Red

### Circuit pattern

- GPIO → resistor → LED anode
- LED cathode → GND

---
# Demo Video

[![Server Demo](https://github.com/user-attachments/assets/cb4f5643-f149-452a-afa2-54f8363e559c)](https://github.com/RyArnz/csc494-smart-media-server/raw/main/Videos/ServerDemo.mp4)

[Click here if the thumbnail does not open](https://github.com/RyArnz/csc494-smart-media-server/raw/main/Videos/ServerDemo.mp4)
---

## Learning With AI

AI was used to:

- assist research
- help troubleshooting
- help document and track changes
- help create Python code

### Workflow

Ask AI for guidance → ask questions → implement manually → test the system → document the verified result

AI mainly helped with:

- Docker/Linux troubleshooting
- reverse proxy design
- monitoring setup
- Raspberry Pi coding

---

## Challenges and Fixes

### Challenges

- getting remote access correct
- understanding reverse proxy vs direct service access
- debugging Grafana “No data” panels
- deciding between LCD display and LEDs
- Raspberry Pi reflash / setup issues

### Fixes

- validated Plex remote access directly
- kept Nextcloud on reverse proxy path
- confirmed Prometheus targets and Grafana datasource
- switched to simpler LED hardware strategy
- rebuilt the Pi from a clean flash

---

## Future Improvements

- extend Raspberry Pi from LEDs to LCD/OLED display
- add alerts and notifications
- expand monitoring into predictive maintenance
- potentially connect with the separate ML monitoring project later

---

# Questions?
