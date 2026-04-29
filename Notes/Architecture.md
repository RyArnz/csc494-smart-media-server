# Architecture

## Overview

This project uses a self-hosted smart media server architecture.

The system combines:

- Ubuntu Server
- Docker containers
- Plex
- Nextcloud
- Nginx Proxy Manager
- Cloudflare Tunnel
- Prometheus
- Grafana
- node_exporter
- cAdvisor
- Raspberry Pi hardware integration

The main purpose of the architecture is to allow multiple self-hosted services to run on one server and be accessed through clean domain names.

---

## Current Repository Architecture

The current GitHub repository is organized around the final project deliverables.

```text
csc494-smart-media-server/
│
├── README.md
├── docker-compose.yml
├── .gitignore
│
├── Images/
│   ├── Cloudflare DNS Management.png
│   ├── Grafana Dashboard.png
│   ├── Nextcloud Dashboard.png
│   ├── Plex Dashboard.png
│   ├── Plex RemoteAccess.png
│   └── Prometheus Endpoints.png
│
├── Notes/
│   ├── Architecture.md
│   ├── Service Notes.md
│   ├── Sprint 2 Progress.md
│   ├── Final Project Summary.md
│   ├── Monitoring Notes.md
│   ├── Raspberry Pi Integration.md
│   └── speakernotes.md
│
├── Slides/
│   ├── Final Presentation.md
│   ├── FinalPresentation.pdf
│   ├── PPP.md
│   ├── PPP_slide.pdf
│   ├── Smart Home Media Server.pdf
│   └── Sprint_1_Media_Server_Presentation.pdf
│
├── Videos/
│   └── ServerDemo.mp4
│
└── scripts/
    ├── raspberry_pi_status.py
    └── example_prometheus_query.py
```

The `Images`, `Notes`, `Slides`, and `Videos` folders match the current repository structure.

---

## High-Level System Architecture

```text
Remote User
    |
    v
Cloudflare DNS
    |
    v
Cloudflare Tunnel
    |
    v
Ubuntu Server
    |
    v
Nginx Proxy Manager
    |
    +-------------------------+
    |                         |
    v                         v
Nextcloud                  Plex
cloud subdomain            media subdomain
```

---

## Monitoring Architecture

```text
Ubuntu Server
    |
    +-------------------------+
    |                         |
    v                         v
node_exporter              cAdvisor
host metrics               container metrics
    |                         |
    +-----------+-------------+
                |
                v
            Prometheus
                |
                v
              Grafana
```

---

## Raspberry Pi Architecture

```text
Prometheus / Server Status
    |
    v
Python Script on Raspberry Pi
    |
    v
LED Output / Physical Status Display
```

---

## Remote Traffic Flow

The remote traffic flow is:

```text
Remote User
    |
    v
Cloudflare
    |
    v
Cloudflare Tunnel
    |
    v
localhost:80 on Ubuntu Server
    |
    v
Nginx Proxy Manager
    |
    v
Correct Docker Container
```

This design allows the project to avoid traditional router port forwarding.

---

## Local Server Flow

Inside the local network, the server runs services in Docker containers.

```text
Ubuntu Server
    |
    v
Docker Engine
    |
    +------------------------------+
    |                              |
    v                              v
Application Containers        Monitoring Containers
Plex / Nextcloud / NPM        Prometheus / Grafana / Exporters
```

---

## Domain Routing

The project uses subdomains to route traffic to different services.

Example:

```text
cloud.arnzenserver.org -> Nextcloud
media.arnzenserver.org -> Plex
```

Cloudflare handles the public DNS side.

Cloudflare Tunnel forwards the traffic to the server.

Nginx Proxy Manager routes the traffic to the correct internal container.

---

## Why Nginx Proxy Manager Is Used

Nginx Proxy Manager allows multiple services to be reached through clean domain names.

Without Nginx Proxy Manager, each service would need to be accessed through a different port.

Example:

```text
Cleaner access:
https://cloud.arnzenserver.org

Instead of:
http://server-ip:8080
```

---

## Why Cloudflare Tunnel Is Used

Cloudflare Tunnel is used because it allows remote access without opening traditional router ports.

This helps simplify the network setup and reduces direct exposure of the home server.

The server makes an outbound tunnel connection to Cloudflare, and Cloudflare forwards requests through that tunnel.

---

## Main Server Role

The Ubuntu server is the center of the project.

It runs:

- Docker
- Plex
- Nextcloud
- Nginx Proxy Manager
- Prometheus
- Grafana
- node_exporter
- cAdvisor
- Supporting database and cache services

The server stores:

- Plex media files
- Nextcloud files
- Application configuration
- Monitoring data
- Docker volumes

---

## Plex Role

Plex is the media server.

It organizes and streams media files stored on the server.

Plex demonstrates:

- Media hosting
- Docker deployment
- Local and remote access
- Reverse proxy routing
- Service troubleshooting

---

## Nextcloud Role

Nextcloud is the private cloud storage service.

It allows files to be uploaded, downloaded, and accessed through a browser.

Nextcloud demonstrates:

- Self-hosted cloud storage
- Web application hosting
- Database-backed Docker service
- Reverse proxy access

---

## Prometheus Role

Prometheus collects metrics from configured targets.

The project uses Prometheus to collect metrics from:

- Prometheus itself
- node_exporter
- cAdvisor

Prometheus provides the data used by Grafana and can also provide data to the Raspberry Pi script.

---

## Grafana Role

Grafana displays Prometheus metrics in dashboards.

Grafana helps show:

- Server CPU usage
- Server RAM usage
- Disk usage
- Container CPU usage
- Container RAM usage
- Prometheus target status

---

## Raspberry Pi Role

The Raspberry Pi acts as a physical status display.

It can check server health and display the result using LEDs.

Example:

```text
Green LED  = Server healthy
Yellow LED = Warning
Red LED    = Critical
Blue LED   = Connection issue
```

---

## Architecture Summary

The most important architecture idea is that the project is not just one service.

It is a connected system:

```text
Docker services + domain routing + secure remote access + monitoring + hardware output
```

This makes the project a complete smart home media server platform.
