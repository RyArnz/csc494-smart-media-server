# CSC 494 Smart Media Server

## Project Overview

This repository documents and supports a self-hosted smart media server project built for CSC 494.

The project combines a home Ubuntu server, Docker containers, reverse proxy routing, secure remote access, media hosting, file hosting, monitoring dashboards, and Raspberry Pi hardware integration into one working system.

The main goal of this project is to build a practical smart home server that can host services locally while still being accessible remotely through a secure domain-based setup.

---

## Project Purpose

The purpose of this project is to demonstrate how a home server can be built, deployed, monitored, and connected to physical hardware.

The project focuses on:

- Hosting a personal media server with Plex
- Hosting a private cloud storage service with Nextcloud
- Using Docker to manage services
- Using Nginx Proxy Manager as a reverse proxy
- Using Cloudflare Tunnel for secure remote access
- Monitoring server health with Prometheus and Grafana
- Sending server status information to a Raspberry Pi

---

## Repository Links

### Main Repository

```text
https://github.com/RyArnz/csc494-smart-media-server
```

This is the main repository for the smart media server project.

### Learning with AI Repository

```text
https://github.com/RyArnz/csc494-iot-ai-learning
```

This repository is separate and will be updated later. It is used for the Learning with AI documentation and topic explanations.

### Separate Monitoring / Machine Learning Repository

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

This is a separate deep learning and monitoring repository. It is related to the server monitoring work.

---

## Main Project Goals

The main goals of this project are:

1. Build a working Ubuntu-based home server
2. Deploy important services using Docker
3. Host Plex for media streaming
4. Host Nextcloud for private file storage
5. Make services accessible through a custom domain
6. Avoid direct router port forwarding by using Cloudflare Tunnel
7. Use Nginx Proxy Manager to route subdomains to the correct services
8. Monitor server health with Prometheus and Grafana
9. Connect a Raspberry Pi to server data

---

## High-Level System Architecture

```text
User Device
    |
    v
Cloudflare DNS / Cloudflare Tunnel
    |
    v
Ubuntu Server
    |
    v
Nginx Proxy Manager
    |
    +--------------------+
    |                    |
    v                    v
Nextcloud             Plex
cloud domain          media domain

Ubuntu Server
    |
    +--------------------+
    |                    |
    v                    v
Prometheus            Grafana
metrics storage       dashboards
    |
    +--------------------+
    |                    |
    v                    v
Node Exporter         cAdvisor
host metrics          container metrics

Prometheus / Server Data
    |
    v
Raspberry Pi
LED / hardware status display
```

---

## Core Technologies Used

| Technology | Purpose |
|---|---|
| Ubuntu Server | Main operating system for the home server |
| Docker | Runs services in containers |
| Docker Compose | Defines and manages multi-container services |
| Plex | Media server for movies, music, and video files |
| Nextcloud | Private cloud storage and file access |
| Nginx Proxy Manager | Reverse proxy for routing domains to services |
| Cloudflare Tunnel | Secure remote access without opening router ports |
| Cloudflare DNS | Domain and subdomain management |
| Prometheus | Time-series metrics collection |
| Grafana | Monitoring dashboards |
| Node Exporter | Host system metrics |
| cAdvisor | Docker container metrics |
| Raspberry Pi | Physical server-status display and hardware integration |
| Python | Used for Raspberry Pi scripts and monitoring logic |

---

## Main Services

## Plex

Plex is used as the media server.

It allows video, music, and other media files stored on the server to be streamed from other devices.

### Plex Role in the Project

Plex demonstrates:

- Self-hosted media streaming
- Dockerized service deployment
- Local and remote access
- Reverse proxy routing through Nginx Proxy Manager
- Service access through a custom domain

### Plex Access Goal

The goal is for Plex to be accessible through a domain such as:

```text
media.arnzenserver.org
```

The exact domain depends on the current DNS and Cloudflare configuration.

---

## Nextcloud

Nextcloud is used as the private cloud file-storage system.

It allows files to be uploaded, downloaded, and accessed through a browser.

### Nextcloud Role in the Project

Nextcloud demonstrates:

- Private cloud hosting
- Dockerized web applications
- File storage on a home server
- Reverse proxy access
- Domain-based routing

### Nextcloud Access Goal

The goal is for Nextcloud to be accessible through a domain such as:

```text
cloud.arnzenserver.org
```

The exact domain depends on the current DNS and Cloudflare configuration.

---

## Nginx Proxy Manager

Nginx Proxy Manager is used as the reverse proxy.

It receives web traffic and forwards it to the correct internal service based on the domain name.

### Example Routing

```text
cloud.arnzenserver.org  ->  Nextcloud
media.arnzenserver.org  ->  Plex
```

### Why Nginx Proxy Manager Is Important

Without a reverse proxy, each service would need to be accessed through separate ports.

With Nginx Proxy Manager, the system can use clean domain names instead of exposing raw service ports.

Example:

```text
Better:
https://cloud.arnzenserver.org

Instead of:
http://server-ip:8080
```

---

## Cloudflare Tunnel

Cloudflare Tunnel is used to provide secure remote access to the server without directly opening router ports.

Instead of forwarding ports from the router to the server, the server runs a Cloudflare tunnel connection outward to Cloudflare.

Remote users connect to Cloudflare, and Cloudflare forwards the traffic through the tunnel to the server.

### Why Cloudflare Tunnel Is Used

Cloudflare Tunnel helps with:

- Avoiding router port forwarding
- Simplifying remote access
- Supporting domain-based service access
- Reducing direct exposure of the home network
- Making the project easier to access from outside the local network

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

### Intended Subdomain Roles

| Subdomain | Service |
|---|---|
| `cloud.arnzenserver.org` | Nextcloud |
| `media.arnzenserver.org` | Plex |

The subdomains are routed through Cloudflare Tunnel to Nginx Proxy Manager, which then forwards traffic to the correct Docker service.

---

## Monitoring Stack

The project includes a monitoring stack to track server health.

The monitoring system is useful for checking whether the server is running correctly and whether containers are using too many resources.

### Monitoring Components

| Component | Purpose |
|---|---|
| Prometheus | Stores and queries time-series metrics |
| Grafana | Displays metrics in dashboards |
| Node Exporter | Provides host CPU, memory, disk, and system metrics |
| cAdvisor | Provides Docker container CPU and memory metrics |

---

## What Prometheus Does

Prometheus collects metrics from configured targets.

In this project, Prometheus collects data from:

- The Ubuntu server through Node Exporter
- Docker containers through cAdvisor
- Prometheus itself for internal health metrics

Prometheus makes it possible to ask questions such as:

- How much CPU is the server using?
- How much RAM is being used?
- How much disk space is left?
- Which containers are using the most resources?
- Are monitoring targets online?

---

## What Grafana Does

Grafana displays Prometheus metrics in dashboards.

Grafana makes it easier to understand the server visually.

Example dashboard information:

- CPU usage
- RAM usage
- Disk usage
- Container CPU usage
- Container memory usage
- Service health
- Metric history over time

---

## Raspberry Pi Integration

The Raspberry Pi is used as a physical hardware extension of the server.

The goal is for the Raspberry Pi to receive or request server status information and display the server state using simple hardware output such as LEDs.

### Raspberry Pi Purpose

The Raspberry Pi integration demonstrates:

- IoT hardware communication
- Python-based server status checks
- Physical output based on server health
- A connection between the home server and an external device

### Example LED Status Idea

```text
Green LED  = Server healthy
Yellow LED = Warning or moderate resource usage
Red LED    = Critical resource usage
Blue LED   = Connection or monitoring issue
```

---

## Current Project Scope

The current project scope includes:

- Ubuntu server setup
- Docker service deployment
- Plex media server
- Nextcloud private cloud
- Nginx Proxy Manager routing
- Cloudflare Tunnel remote access
- Prometheus metrics collection
- Grafana dashboards
- Raspberry Pi server-status integration
- GitHub documentation
- Final presentation and demo support

---

## What This Repository Should Contain

A good final version of this repository should contain:

```text
csc494-smart-media-server/
│
├── README.md
├── docker-compose.yml
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── setup-guide.md
│   ├── service-notes.md
│   ├── troubleshooting.md
│   ├── sprint-two-notes.md
│   ├── final-project-summary.md
│   └── future-work.md
│
├── scripts/
│   ├── raspberry_pi_status.py
│   └── example_prometheus_query.py
│
├── images/
│   ├── architecture-diagram.png
│   ├── grafana-dashboard.png
│   ├── plex-access.png
│   └── nextcloud-access.png
│
├── slides/
│   └── final-presentation.md
│
└── demo/
    └── demo-video-notes.md
```

The exact file names can vary, but the repository should clearly separate documentation, scripts, images, slides, and configuration files.

---

## Recommended Documentation Files

This repository should include the following documentation files.

### `README.md`

Main project overview and starting point.

### `docs/architecture.md`

Explains the system architecture, including Docker, Nginx Proxy Manager, Cloudflare Tunnel, Plex, Nextcloud, Prometheus, Grafana, and Raspberry Pi integration.

### `docs/setup-guide.md`

Explains how the server was set up and how services were deployed.

### `docs/service-notes.md`

Explains the purpose of each major service.

### `docs/troubleshooting.md`

Documents problems encountered and how they were solved.

### `docs/sprint-two-notes.md`

Documents Sprint Two progress and accomplishments.

### `docs/final-project-summary.md`

Summarizes the final completed system.

### `docs/future-work.md`

Explains how the project could be improved later.

---

## Setup Overview

This section gives a general setup overview.

Exact commands may vary depending on the server, file paths, and Docker Compose files.

### 1. Install Ubuntu Server

Install Ubuntu Server on the machine that will host the project.

The server should have:

- Network access
- SSH access
- Enough storage for media and cloud files
- Docker installed
- Docker Compose installed

---

### 2. Install Docker

Example install check:

```bash
docker --version
docker compose version
```

---

### 3. Create Project Folders

Example folder layout:

```bash
mkdir -p ~/docker
mkdir -p /data/media
mkdir -p /data/nextcloud
mkdir -p /data/plex/config
```
---

### 4. Deploy Docker Services

Services should be deployed using Docker Compose.

Common project services include:

- Nginx Proxy Manager
- Plex
- Nextcloud
- MariaDB
- Redis
- Prometheus
- Grafana
- Node Exporter
- cAdvisor

Example command:

```bash
docker compose up -d
```

---

### 5. Verify Containers

Check running containers:

```bash
docker ps
```

Check container logs:

```bash
docker logs container_name
```

Restart a container:

```bash
docker restart container_name
```

---

### 6. Configure Nginx Proxy Manager

Nginx Proxy Manager should route each subdomain to the correct internal service.

Example proxy hosts:

```text
cloud.arnzenserver.org -> Nextcloud internal service
media.arnzenserver.org -> Plex internal service
```

---

### 7. Configure Cloudflare Tunnel

Cloudflare Tunnel should forward domain traffic to the local server.

A simplified tunnel flow looks like this:

```text
Cloudflare DNS
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
Correct Docker service
```

---

### 8. Configure Monitoring

Prometheus should scrape:

- Node Exporter
- cAdvisor
- Prometheus itself

Grafana should use Prometheus as a data source.

---

### 9. Connect Raspberry Pi

The Raspberry Pi should run a Python script that checks server status or Prometheus metrics and changes hardware output based on the result.

Example:

```text
Prometheus metric -> Python script -> LED status
```

---

## Common Commands

### Check Running Containers

```bash
docker ps
```

### Check All Containers

```bash
docker ps -a
```

### Restart a Container

```bash
docker restart container_name
```

### View Container Logs

```bash
docker logs container_name
```

### Follow Container Logs

```bash
docker logs -f container_name
```

### Start Docker Compose Stack

```bash
docker compose up -d
```

### Stop Docker Compose Stack

```bash
docker compose down
```

### Check Open Ports

```bash
ss -lntp
```

### Check Server IP Address

```bash
ip addr
```

### Test Local HTTP Response

```bash
curl -I http://localhost
```

### Test Prometheus

```bash
curl http://localhost:9090/-/ready
```

---

## Service Verification Checklist

Use this checklist to verify the project.

### Server

- [ ] Ubuntu Server boots correctly
- [ ] Server has network access
- [ ] SSH access works
- [ ] Docker is installed
- [ ] Docker Compose is installed

### Docker

- [ ] Required containers are running
- [ ] Containers restart correctly
- [ ] Volumes are mapped correctly
- [ ] Services are on the correct Docker networks

### Plex

- [ ] Plex container is running
- [ ] Plex is reachable locally
- [ ] Plex libraries are mapped to the correct media folders
- [ ] Plex can scan media
- [ ] Plex is reachable through the media subdomain

### Nextcloud

- [ ] Nextcloud container is running
- [ ] Database container is running
- [ ] Redis container is running, if used
- [ ] Nextcloud is reachable locally
- [ ] Nextcloud is reachable through the cloud subdomain
- [ ] File upload and download works

### Nginx Proxy Manager

- [ ] Nginx Proxy Manager container is running
- [ ] Admin interface is reachable
- [ ] Proxy host for Nextcloud exists
- [ ] Proxy host for Plex exists
- [ ] Hostnames point to the correct internal services

### Cloudflare Tunnel

- [ ] Tunnel service is running
- [ ] Tunnel routes to the server
- [ ] Cloudflare DNS records exist
- [ ] Subdomains route to Nginx Proxy Manager
- [ ] Remote access works outside the local network

### Prometheus

- [ ] Prometheus container is running
- [ ] Prometheus web UI is reachable
- [ ] Node Exporter target is up
- [ ] cAdvisor target is up
- [ ] Prometheus self-target is up

### Grafana

- [ ] Grafana container is running
- [ ] Grafana web UI is reachable
- [ ] Prometheus data source is connected
- [ ] Dashboards display metrics

### Raspberry Pi

- [ ] Raspberry Pi boots correctly
- [ ] Python script runs
- [ ] Server connection works
- [ ] LEDs or output devices respond correctly
- [ ] Status logic matches server conditions

---

## Problems Encountered and Fixes

## Problem 1: Plex Was Not Available Externally

### Issue

Plex worked locally but was not correctly available from outside the network.

### Cause

The project needed correct routing between:

```text
Cloudflare Tunnel -> Nginx Proxy Manager -> Plex container
```

The issue was not just whether Plex itself was running. The remote path had to be configured correctly.

### Fix

The routing was corrected so that the media subdomain pointed through Cloudflare Tunnel to Nginx Proxy Manager, and Nginx Proxy Manager forwarded the request to the Plex service.

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

This project avoids direct router port forwarding by using Cloudflare Tunnel.

This improves the remote access design because the server does not need to expose multiple public ports directly to the internet.

Important security practices:

- Use strong passwords
- Keep Docker images updated
- Do not commit `.env` files
- Do not expose admin panels unnecessarily
- Use HTTPS where possible
- Restrict admin interfaces when possible
- Keep Cloudflare and Nginx Proxy Manager settings organized

---

## Files That Should Not Be Committed

The repository should not include private secrets, passwords, large media files, or local machine-specific data.

Recommended `.gitignore` entries:

```gitignore
# Environment files
.env
*.env

# System files
.DS_Store
Thumbs.db

# Logs
*.log

# Docker / local data
data/
config/
letsencrypt/
mysql/
mariadb/
redis/

# Media files
*.mp4
*.mkv
*.avi
*.mov
*.mp3
*.flac

# Python
__pycache__/
*.pyc
.venv/
venv/

# Large exports
*.zip
*.tar
*.gz

---

## Suggested Repository Structure

```text
csc494-smart-media-server/
│
├── README.md
├── .gitignore
├── docker-compose.example.yml
│
├── docs/
│   ├── architecture.md
│   ├── setup-guide.md
│   ├── service-notes.md
│   ├── troubleshooting.md
│   ├── sprint-two-notes.md
│   ├── final-project-summary.md
│   └── future-work.md
│
├── scripts/
│   ├── raspberry_pi_status.py
│   └── example_prometheus_query.py
│
├── images/
│   ├── architecture-diagram.png
│   ├── grafana-dashboard.png
│   ├── plex-access.png
│   └── nextcloud-access.png
│
├── slides/
│   └── final-presentation.md
│
└── demo/
    └── demo-video-notes.md
```

---

## Sprint Two Notes

## Sprint Two Overview

Sprint Two focused on building the working server foundation and connecting the major services.

The work moved the project from an idea into a functional home server environment.

---

## Sprint Two Goals

The main Sprint Two goals were:

1. Deploy the main server services
2. Confirm Docker containers were running
3. Configure Plex
4. Configure Nextcloud
5. Set up remote access through Cloudflare Tunnel
6. Route domains through Nginx Proxy Manager
7. Begin monitoring the server with Prometheus and Grafana
8. Start Raspberry Pi integration planning
9. Document problems and fixes

---

## Sprint Two Completed Work

### Server Setup

The Ubuntu server was configured as the main host machine for the project.

Docker was used to run the services in containers.

---

### Plex Setup

Plex was deployed and configured as the media server.

The project verified that Plex could run locally and then worked toward making it available remotely through the media domain.

---

### Nextcloud Setup

Nextcloud was deployed and configured as the private cloud storage service.

The project verified that files could be uploaded and downloaded through the web interface.

---

### Reverse Proxy Setup

Nginx Proxy Manager was used to manage service routing.

This made it possible to route different subdomains to different services.

---

### Cloudflare Tunnel Setup

Cloudflare Tunnel was used to provide remote access without traditional router port forwarding.

This became one of the most important parts of the project because it allowed the server to be accessed remotely while keeping the network setup cleaner.

---

### Monitoring Setup

Prometheus and Grafana were added to monitor the server.

Node Exporter and cAdvisor were used to collect host and container metrics.

---

### Raspberry Pi Planning

The project began connecting the server to a Raspberry Pi so the Pi could display server status using physical hardware output.

---

## Sprint Two Results

By the end of Sprint Two, the project had:

- A working Ubuntu server
- Docker containers running
- Plex deployed
- Nextcloud deployed
- Nginx Proxy Manager routing services
- Cloudflare Tunnel supporting remote access
- Prometheus collecting server metrics
- Grafana showing dashboards
- A plan for Raspberry Pi server-status integration
- AI model trained on server telemtry

---

## Sprint Two Reflection

Sprint Two was important because it turned the project into a working system.

The biggest progress was getting system monitoring working and setup for the server. During sprint two I deployed grafana, cadvisor, and prometheus for server monitoring. AI models were trained on server telemtry. Plex cloud was fix and is now working externally. 

---

## Final Project Summary

This project successfully demonstrates a self-hosted smart media server environment.

The system combines media streaming, private cloud storage, secure remote access, monitoring, and hardware integration.

The project shows how the server infrastructure is built and maintained. It includes networking, containers, reverse proxies, monitoring, troubleshooting, and documentation.

---

## Current Limitations

Current limitations include:

1. Some setup steps are specific to the current home server
2. Some private configuration values cannot be committed to GitHub
3. Remote access depends on Cloudflare Tunnel configuration
4. Not all media files are not included in the repository
5. Monitoring is useful, but alerting can still be improved

---

## Future Work

Future improvements include:

- Add more screenshot
- Add a full architecture diagram
- Add a sanitized Docker Compose example
- Add Grafana dashboard screenshots
- Add service backup instructions
- Add automatic container update notes
- Add health-check scripts
- Add alerting through Grafana
- Add a more polished final demo video

---

## Related AI / Monitoring Extension

A separate repository exists for deeper machine learning and monitoring work:

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

That repository focuses on collecting Prometheus metrics and using them for deep learning experiments.

---

## Learning with AI Extension

The Learning with AI repository is separate:

```text
https://github.com/RyArnz/csc494-iot-ai-learning
```

That repository will be updated later with AI learning reflections, topic writeups, and supporting class documentation.

---





