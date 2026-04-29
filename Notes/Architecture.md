# Architecture

## Overview

This project uses a self-hosted smart media server architecture.

The system combines a home Ubuntu server, Docker containers, reverse proxy routing, Cloudflare Tunnel remote access, Plex media hosting, Nextcloud file hosting, Prometheus/Grafana monitoring, and Raspberry Pi hardware integration.

The main purpose of this architecture is to allow multiple services to run on one home server while still being accessible through clean domain names.

---

## Current Repository Architecture

The current repository is organized around the final project documentation, screenshots, slides, and demo files.

```text
csc494-smart-media-server/
│
├── README.md
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
└── Videos/
    └── ServerDemo.mp4
```

This layout separates the project into documentation, screenshots, presentation files, and demo evidence.

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
cloud.arnzenserver.org     media.arnzenserver.org
```

This is the main traffic path for remote access.

Cloudflare handles the public domain side.

Cloudflare Tunnel forwards traffic to the home server.

Nginx Proxy Manager receives the request and routes it to the correct internal service.

---

## Local Server Architecture

```text
Ubuntu Server
    |
    v
Docker
    |
    +-----------------------------+
    |                             |
    v                             v
Application Services          Monitoring Services
Plex / Nextcloud / NPM        Prometheus / Grafana / Exporters
```

The Ubuntu server is the physical or main host machine.

Docker is used to run each service in a container so the services remain easier to manage and isolate.

---

## Application Service Architecture

```text
Docker Network
    |
    +-------------------------+
    |                         |
    v                         v
Plex                      Nextcloud
Media streaming           Private cloud storage
    |                         |
    v                         v
/data/media               Nextcloud data + database
```

Plex provides the media server portion of the project.

Nextcloud provides the private cloud storage portion of the project.

Both services are routed through Nginx Proxy Manager for cleaner public access.

---

## Reverse Proxy Architecture

```text
Incoming Domain Request
    |
    v
Nginx Proxy Manager
    |
    +------------------------------------+
    |                                    |
    v                                    v
cloud.arnzenserver.org               media.arnzenserver.org
Forward to Nextcloud                 Forward to Plex
```

Nginx Proxy Manager is important because it allows multiple services to share the same public entry point.

Instead of accessing services with different ports, users can access them with clear subdomains.

Example:

```text
cloud.arnzenserver.org  ->  Nextcloud
media.arnzenserver.org  ->  Plex
```

---

## Cloudflare Tunnel Architecture

```text
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
```

Cloudflare Tunnel allows the home server to be reached remotely without traditional router port forwarding.

The tunnel creates an outbound connection from the server to Cloudflare. Remote users connect to Cloudflare, and Cloudflare forwards the traffic through the tunnel to the local server.

This makes the remote access setup cleaner and avoids exposing multiple services directly through router port forwarding.

---

## Monitoring Architecture

```text
Ubuntu Server
    |
    +--------------------------+
    |                          |
    v                          v
Node Exporter                 cAdvisor
Host metrics                  Docker container metrics
    |                          |
    +------------+-------------+
                 |
                 v
             Prometheus
                 |
                 v
              Grafana
```

The monitoring stack allows the project to track server health.

Prometheus collects metrics.

Grafana displays the metrics in dashboards.

Node Exporter provides host-level metrics.

cAdvisor provides Docker container metrics.

---

## Monitoring Targets

Prometheus monitors several targets.

```text
Prometheus      -> monitors itself
Node Exporter   -> monitors Ubuntu host metrics
cAdvisor        -> monitors Docker container metrics
```

Prometheus scrapes itself so it can report its own health and performance.

This makes it easier to verify that the monitoring system is working.

---

## Raspberry Pi Architecture

```text
Prometheus / Server Status
    |
    v
Python Script on Raspberry Pi
    |
    v
LED Status Output
```

The Raspberry Pi extends the project into a physical IoT-style display.

The Pi can check server status data and display the result using LEDs.

Example LED logic:

```text
Green LED  = Server healthy
Yellow LED = Warning condition
Red LED    = Critical condition
Blue LED   = Connection or monitoring problem
```

---

## Complete Project Flow

```text
User opens cloud or media subdomain
    |
    v
Cloudflare DNS resolves the domain
    |
    v
Cloudflare Tunnel forwards traffic to the server
    |
    v
Nginx Proxy Manager receives the request
    |
    v
Nginx Proxy Manager forwards to Plex or Nextcloud
    |
    v
Prometheus monitors the server and containers
    |
    v
Grafana displays dashboards
    |
    v
Raspberry Pi can show physical server status
```

---

## Current Project Evidence

The repository includes screenshots and files that show the system working.

```text
Images/Cloudflare DNS Management.png
Images/Grafana Dashboard.png
Images/Nextcloud Dashboard.png
Images/Plex Dashboard.png
Images/Plex RemoteAccess.png
Images/Prometheus Endpoints.png
Videos/ServerDemo.mp4
```

These files support the final project by showing the working services, monitoring dashboard, remote access, and project demo.

---

## Why This Architecture Works

This architecture works because each part has a clear responsibility.

| Component | Responsibility |
|---|---|
| Ubuntu Server | Hosts the full system |
| Docker | Runs services in containers |
| Plex | Provides media streaming |
| Nextcloud | Provides private cloud storage |
| Nginx Proxy Manager | Routes domains to services |
| Cloudflare Tunnel | Provides remote access |
| Prometheus | Collects metrics |
| Grafana | Displays dashboards |
| Raspberry Pi | Provides physical status output |

---

## Main Architecture Lesson

The most important lesson from this architecture is that remote access requires the entire route to be correct.

A service can work locally but still fail remotely if any part of this chain is wrong:

```text
Cloudflare -> Cloudflare Tunnel -> Nginx Proxy Manager -> Docker service
```

Understanding that chain made it possible to troubleshoot Plex, Nextcloud, and the monitoring tools.

---

## Related Repository Note

The separate monitoring and machine learning repository is:

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

That repository is related to the Prometheus monitoring work, but this repository focuses on the smart media server infrastructure itself.
