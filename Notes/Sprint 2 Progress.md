
# Sprint 2 Progress

## Sprint 2 Overview

Sprint 2 focused on turning the smart media server from a basic setup into a working connected system.

The main goal was to get the core services running, make them accessible through domain-based routing, add monitoring, and begin connecting server data to Raspberry Pi hardware output.

By the end of Sprint 2, the project had a working foundation for a self-hosted smart home media server.

---

## Sprint 2 Goals

The main Sprint 2 goals were:

1. Set up and organize the Ubuntu server environment
2. Deploy major services with Docker
3. Configure Plex as the media server
4. Configure Nextcloud as the private cloud service
5. Configure Nginx Proxy Manager for reverse proxy routing
6. Configure Cloudflare Tunnel for remote access
7. Confirm services could be reached through custom subdomains
8. Add Prometheus for server and container metrics
9. Add Grafana dashboards for monitoring
10. Plan and begin Raspberry Pi hardware integration
11. Document issues, fixes, screenshots, and project progress

---

## Completed Work

## 1. Ubuntu Server Setup

The Ubuntu server was used as the main host for the project.

The server is responsible for running Docker, storing files, hosting services, and supporting remote access.

Completed server work included:

- Preparing the server environment
- Using the command line for management
- Organizing media and service storage
- Running Docker containers
- Testing local service access

---

## 2. Docker Service Deployment

Docker was used to run the project services in containers.

This made the system easier to manage because each major service could run separately while still being connected through Docker networking.

Services deployed or used during Sprint 2 included:

- Plex
- Nextcloud
- MariaDB
- Redis
- Nginx Proxy Manager
- Prometheus
- Grafana
- Node Exporter
- cAdvisor

---

## 3. Plex Media Server Setup

Plex was configured as the media server portion of the project.

The goal was to allow media files stored on the server to be streamed from other devices.

Plex work included:

- Running Plex on the server
- Connecting Plex to server media folders
- Confirming local Plex access
- Troubleshooting remote access
- Routing the media subdomain to Plex
- Capturing Plex dashboard and remote access screenshots

Evidence in the repository includes:

```text
Images/Plex Dashboard.png
Images/Plex RemoteAccess.png
```

---

## 4. Nextcloud Setup

Nextcloud was configured as the private cloud storage portion of the project.

The goal was to allow files to be uploaded, downloaded, and accessed through a browser.

Nextcloud work included:

- Running Nextcloud on the server
- Using supporting services such as MariaDB and Redis
- Confirming the Nextcloud dashboard loaded
- Testing browser-based file access
- Routing the cloud subdomain to Nextcloud
- Capturing a Nextcloud screenshot

Evidence in the repository includes:

```text
Images/Nextcloud Dashboard.png
```

---

## 5. Nginx Proxy Manager Setup

Nginx Proxy Manager was used as the reverse proxy.

The purpose of Nginx Proxy Manager is to route domain traffic to the correct internal service.

Example routing:

```text
cloud.arnzenserver.org -> Nextcloud
media.arnzenserver.org -> Plex
```

This allowed the project to use clean service names instead of accessing services by raw IP address and port.

---

## 6. Cloudflare Tunnel Setup

Cloudflare Tunnel was used to support remote access without traditional router port forwarding.

The remote access path is:

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
    v
Plex or Nextcloud
```

This became one of the most important parts of the project because it allowed the services to be reached remotely while keeping the home network setup cleaner.

Evidence in the repository includes:

```text
Images/Cloudflare DNS Management.png
```

---

## 7. Monitoring Stack Setup

Prometheus and Grafana were added so the server could be monitored.

The monitoring stack includes:

- Prometheus
- Grafana
- Node Exporter
- cAdvisor

Prometheus collects metrics.

Grafana displays the metrics in dashboards.

Node Exporter provides host server metrics.

cAdvisor provides Docker container metrics.

Evidence in the repository includes:

```text
Images/Prometheus Endpoints.png
Images/Grafana Dashboard.png
```

---

## 8. Raspberry Pi Integration Planning

The Raspberry Pi was planned as the physical hardware extension of the project.

The purpose of the Raspberry Pi is to display server status using physical output such as LEDs.

Planned LED behavior:

```text
Green LED  = Server healthy
Yellow LED = Warning
Red LED    = Critical issue
Blue LED   = Connection or monitoring issue
```

The Raspberry Pi connects the server project to IoT concepts by turning server health into a physical status display.

---

## Problems Encountered and Solved

## Problem 1: Plex Worked Locally but Not Remotely

### Issue

Plex was reachable locally, but it was not correctly reachable outside the local network.

### Cause

The service itself was running, but the remote access path was not fully correct.

The required path was:

```text
Cloudflare -> Cloudflare Tunnel -> Nginx Proxy Manager -> Plex
```

### Fix

The media subdomain was routed through Cloudflare Tunnel to Nginx Proxy Manager, and Nginx Proxy Manager was configured to forward that traffic to Plex.

### Result

Plex became reachable through the media domain.

---

## Problem 2: Media Domain Showed the Wrong Page

### Issue

The media domain reached the server, but it showed the wrong page instead of Plex.

### Cause

The request was making it to the server, but Nginx Proxy Manager was not routing that hostname to Plex correctly.

### Fix

The proxy host rule for the media domain was corrected.

### Result

The media domain loaded Plex instead of the wrong page.

---

## Problem 3: Grafana Did Not Show Useful Dashboards at First

### Issue

Grafana was running, but the dashboard did not show useful monitoring data at first.

### Cause

Grafana needs Prometheus configured as a data source, and Prometheus needs working scrape targets.

### Fix

Prometheus targets were checked, and the Grafana data source/dashboard setup was corrected.

### Result

Grafana displayed server and container monitoring data.

---

## Problem 4: Understanding Prometheus Targets

### Issue

It was unclear why Prometheus had multiple targets and why it scraped itself.

### Explanation

Prometheus targets are endpoints that Prometheus collects metrics from.

In this project, the targets include:

```text
Prometheus itself
Node Exporter
cAdvisor
```

Prometheus scrapes itself so it can monitor its own health.

### Result

The monitoring stack became easier to explain and troubleshoot.

---

## Sprint 2 Results

By the end of Sprint 2, the project had:

- A working Ubuntu-based server foundation
- Docker services running
- Plex deployed
- Nextcloud deployed
- Cloudflare Tunnel remote access configured
- Nginx Proxy Manager routing services by domain
- Prometheus collecting metrics
- Grafana displaying dashboards
- Raspberry Pi integration planned
- Screenshots added to the repository
- Project documentation started

---

## Repository Evidence Added

Sprint 2 documentation and evidence includes:

```text
Images/Cloudflare DNS Management.png
Images/Grafana Dashboard.png
Images/Nextcloud Dashboard.png
Images/Plex Dashboard.png
Images/Plex RemoteAccess.png
Images/Prometheus Endpoints.png
Videos/ServerDemo.mp4
Notes/Architecture.md
Notes/Service Notes.md
Notes/Sprint 2 Progress.md
Notes/Final Project Summary.md
```

These files show the system components, progress, and final project state.

---

## What Was Learned

Sprint 2 showed that a server project is not just about running individual applications.

The most important lesson was understanding how the full system connects:

```text
Domain -> Cloudflare -> Tunnel -> Reverse Proxy -> Docker Service
```

Once that path was understood, it became much easier to troubleshoot remote access problems.

Sprint 2 also showed the importance of monitoring. Prometheus and Grafana made it possible to see whether the server and containers were actually healthy instead of guessing.

---

## Sprint 2 Reflection

Sprint 2 was the point where the project became a real working system.

The project moved beyond installing services and became a connected smart media server with remote access, monitoring, and hardware integration planning.

The biggest success was getting the services to work together through Cloudflare Tunnel and Nginx Proxy Manager.

The biggest challenge was troubleshooting routing issues where a service worked locally but not remotely.

---


