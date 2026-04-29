# CSC 494 Smart Media Server

## Project Overview

This repository documents a completed self-hosted smart media server project built for CSC 494.

The project combines an Ubuntu Server, Docker-based services, reverse proxy routing, secure remote access, media hosting, private cloud storage, server monitoring, final presentation materials, and a demo video into one documented system.

The completed system demonstrates how a home server can host useful local services while still being accessible remotely through a secure domain-based setup.

---

## Project Purpose

The purpose of this project is to show how a home server can be built, deployed, monitored, and documented as a working smart media server system.

The project includes:

- Plex for media streaming
- Nextcloud for private cloud storage
- Docker-based service deployment
- Nginx Proxy Manager reverse proxy routing
- Cloudflare Tunnel remote access
- Prometheus and Grafana monitoring
- Raspberry Pi hardware status integration
- Final screenshots, notes, slides, and demo video evidence

---

## Repository Structure

The final repository is organized as follows:

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
│   ├── Final Presentation
│   ├── Final Project Summary.md
│   ├── Monitoring Notes.md
│   ├── NOTES
│   ├── Raspberry Pi Integration.md
│   ├── Service Notes.md
│   ├── Sprint 2 Progress
│   ├── Sprint1-notes
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

---

## Main Project Goals

The completed project demonstrates the following goals:

1. Build an Ubuntu-based home server
2. Deploy useful self-hosted services
3. Host Plex for media streaming
4. Host Nextcloud for private file storage
5. Make services accessible through a custom domain
6. Use Cloudflare Tunnel instead of traditional router port forwarding
7. Use Nginx Proxy Manager to route subdomains to the correct services
8. Monitor server health with Prometheus and Grafana
9. Connect server status information to Raspberry Pi hardware
10. Document the completed system with screenshots, notes, slides, and a demo video

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

Cloudflare handles public DNS.

Cloudflare Tunnel forwards remote traffic to the home server.

Nginx Proxy Manager receives the incoming request and routes it to the correct internal service.

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

Prometheus collects metrics from the server and containers.

Grafana displays those metrics in dashboards.

Node Exporter provides host-level server metrics.

cAdvisor provides Docker container metrics.

---

## Raspberry Pi Hardware Integration

```text
Prometheus / Server Status
    |
    v
Raspberry Pi
    |
    v
LED / Hardware Status Display
```

The Raspberry Pi acts as a physical hardware extension of the server.

The Raspberry Pi integration shows how server status can be represented through physical output instead of only through a web dashboard.

Example status behavior:

```text
Green LED  = Server healthy
Yellow LED = Warning or moderate resource usage
Red LED    = Critical resource usage
Blue LED   = Connection or monitoring issue
```

---

## Core Technologies Used

| Technology | Purpose |
|---|---|
| Ubuntu Server | Main operating system for the home server |
| Docker | Runs services in containers |
| Plex | Media server for video, music, and other media files |
| Nextcloud | Private cloud storage and file access |
| Nginx Proxy Manager | Reverse proxy for routing domains to services |
| Cloudflare Tunnel | Secure remote access without traditional router port forwarding |
| Cloudflare DNS | Domain and subdomain management |
| Prometheus | Time-series metrics collection |
| Grafana | Monitoring dashboards |
| Node Exporter | Host system metrics |
| cAdvisor | Docker container metrics |
| Raspberry Pi | Physical server-status display and hardware integration |

---

## Main Services

## Plex

Plex is used as the media server.

It allows video, music, and other media files stored on the server to be streamed from other devices.

Plex demonstrates:

- Self-hosted media streaming
- Dockerized service deployment
- Local and remote access
- Reverse proxy routing through Nginx Proxy Manager
- Service access through a custom domain

Repository evidence:

```text
Images/Plex Dashboard.png
Images/Plex RemoteAccess.png
```

---

## Nextcloud

Nextcloud is used as the private cloud file-storage system.

It allows files to be uploaded, downloaded, and accessed through a browser.

Nextcloud demonstrates:

- Private cloud hosting
- Dockerized web application deployment
- File storage on a home server
- Reverse proxy access
- Domain-based routing

Repository evidence:

```text
Images/Nextcloud Dashboard.png
```

---

## Nginx Proxy Manager

Nginx Proxy Manager is used as the reverse proxy.

It receives web traffic and forwards it to the correct internal service based on the domain name.

Example routing:

```text
cloud.arnzenserver.org  ->  Nextcloud
media.arnzenserver.org  ->  Plex
```

Nginx Proxy Manager allows the project to use clean domain names instead of raw IP addresses and port numbers.

---

## Cloudflare Tunnel

Cloudflare Tunnel provides remote access without traditional router port forwarding.

Instead of opening router ports directly to the server, the server maintains a tunnel connection to Cloudflare.

Remote users connect through Cloudflare, and Cloudflare forwards traffic through the tunnel to the server.

Repository evidence:

```text
Images/Cloudflare DNS Management.png
```

---

## Prometheus

Prometheus collects metrics from configured targets.

In this project, Prometheus collects data from:

- Prometheus itself
- Node Exporter
- cAdvisor

Prometheus makes it possible to check server and monitoring health through metric endpoints.

Repository evidence:

```text
Images/Prometheus Endpoints.png
```

---

## Grafana

Grafana displays Prometheus metrics in dashboards.

Grafana makes it easier to understand the server visually by showing graphs and monitoring panels for server and container activity.

Repository evidence:

```text
Images/Grafana Dashboard.png
```

---

## Domain and Subdomain Structure

The project uses a custom domain for remote access.

Example domain:

```text
arnzenserver.org
```

Example subdomains:

```text
cloud.arnzenserver.org
media.arnzenserver.org
```

| Subdomain | Service |
|---|---|
| `cloud.arnzenserver.org` | Nextcloud |
| `media.arnzenserver.org` | Plex |

The subdomains are routed through Cloudflare Tunnel to Nginx Proxy Manager, which forwards traffic to the correct internal service.

---

## Project Evidence

The repository includes screenshots, notes, slides, and a demo video.

## Screenshots

```text
Images/Cloudflare DNS Management.png
Images/Grafana Dashboard.png
Images/Nextcloud Dashboard.png
Images/Plex Dashboard.png
Images/Plex RemoteAccess.png
Images/Prometheus Endpoints.png
```

## Notes

```text
Notes/Architecture.md
Notes/Final Presentation
Notes/Final Project Summary.md
Notes/Monitoring Notes.md
Notes/NOTES
Notes/Raspberry Pi Integration.md
Notes/Service Notes.md
Notes/Sprint 2 Progress
Notes/Sprint1-notes
Notes/speakernotes.md
```

## Slides

```text
Slides/Final Presentation.md
Slides/FinalPresentation.pdf
Slides/PPP.md
Slides/PPP_slide.pdf
Slides/Smart Home Media Server.pdf
Slides/Sprint_1_Media_Server_Presentation.pdf
```

## Demo Video

```text
Videos/ServerDemo.mp4
```

---

## Problems Encountered and Fixes

## Problem 1: Plex Was Not Available Externally

### Issue

Plex worked locally but was not correctly available from outside the network.

### Cause

The project needed correct routing between:

```text
Cloudflare Tunnel -> Nginx Proxy Manager -> Plex
```

The issue was not only whether Plex itself was running. The full remote access path had to be configured correctly.

### Fix

The routing was corrected so that the media subdomain pointed through Cloudflare Tunnel to Nginx Proxy Manager, and Nginx Proxy Manager forwarded the request to Plex.

### Result

Plex became accessible through the configured media domain.

---

## Problem 2: Nginx Welcome Page Appeared Instead of Plex

### Issue

The media domain showed the wrong page instead of Plex.

### Cause

The domain was reaching the server, but Nginx Proxy Manager was not routing the hostname to the correct Plex service.

### Fix

The Nginx Proxy Manager proxy host for the media subdomain was corrected.

### Result

The media domain routed to Plex instead of the default Nginx page.

---

## Problem 3: Grafana Dashboards Were Not Showing Correctly

### Issue

Grafana was running, but dashboards did not show useful metrics at first.

### Cause

Grafana needs Prometheus configured as a data source, and Prometheus must have working scrape targets.

### Fix

The Prometheus data source and dashboard configuration were checked and corrected.

### Result

Grafana dashboards displayed server and container metrics correctly.

---

## Security Notes

This project uses Cloudflare Tunnel instead of traditional router port forwarding.

This improves the remote access design because the server does not need to expose multiple public service ports directly to the internet.

The repository avoids storing private credentials and separates project documentation from private deployment values.

Sensitive values that should stay private include:

- Passwords
- Private keys
- Cloudflare tunnel credentials
- API tokens
- Database passwords
- Personal media files
- Private configuration files

---

## Related Repositories

This repository is the main CSC 494 smart media server project.

The related Learning with AI repository is separate:

```text
https://github.com/RyArnz/csc494-iot-ai-learning
```

The separate monitoring and machine learning repository is also separate:

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

Those repositories support related coursework and monitoring work, but this repository focuses on the smart media server system.

---

## Final Project Summary

This project demonstrates a working self-hosted smart media server environment.

The system combines media streaming, private cloud storage, secure remote access, monitoring, and Raspberry Pi hardware integration.

The project shows how server infrastructure can be built and maintained using Linux, Docker-based services, reverse proxy routing, Cloudflare Tunnel, Prometheus, Grafana, and hardware-based status output.

The final result is a smart home media server that hosts useful services locally, exposes them remotely through a controlled domain-based setup, and provides monitoring evidence through dashboards and project screenshots.
