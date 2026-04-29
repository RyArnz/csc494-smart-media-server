# Architecture

## Overview

This project uses a self-hosted smart media server architecture.

The system combines a home Ubuntu server, Docker containers, domain-based routing, secure remote access, monitoring, and Raspberry Pi hardware integration.

The main purpose of the architecture is to allow multiple self-hosted services to run on one server and be accessed through clean domain names.

---

## High-Level Architecture

```text
User Device
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
    +--------------------+
    |                    |
    v                    v
Nextcloud             Plex
cloud domain          media domain
```

---

## Monitoring Architecture

```text
Ubuntu Server
    |
    +--------------------+
    |                    |
    v                    v
Node Exporter         cAdvisor
Host Metrics          Container Metrics
    |                    |
    +---------+----------+
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

## Traffic Flow

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
localhost:80 on the Ubuntu Server
    |
    v
Nginx Proxy Manager
    |
    v
Correct Docker Container
```

This allows the project to avoid traditional router port forwarding.

---

## Main Server

The Ubuntu server is the center of the project.

The server runs:

- Docker
- Plex
- Nextcloud
- Nginx Proxy Manager
- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Supporting database/cache containers

The server stores media files and cloud files.

---

## Docker

Docker is used to run the services in containers.

This keeps the services separated and makes the setup easier to manage.

Benefits of Docker in this project:

- Easier service deployment
- Easier restarts
- Isolated service environments
- Clear volume mappings
- Easier backup planning
- Easier migration later

---

## Nginx Proxy Manager

Nginx Proxy Manager is the reverse proxy.

It receives traffic and decides which internal service should receive the request.

Example:

```text
cloud.arnzenserver.org -> Nextcloud
media.arnzenserver.org -> Plex
```

Without Nginx Proxy Manager, services would need to be accessed by IP address and port number.

---

## Cloudflare Tunnel

Cloudflare Tunnel provides remote access to the server without opening router ports.

The server creates an outbound tunnel connection to Cloudflare.

Cloudflare then forwards incoming domain traffic through the tunnel to the server.

This helps keep the home network cleaner and reduces the need for direct public port exposure.

---

## Plex

Plex is the media server.

It uses server storage folders to organize and stream media.

Plex demonstrates:

- Media hosting
- Dockerized service deployment
- Local and remote access
- Domain routing through Nginx Proxy Manager

---

## Nextcloud

Nextcloud is the private cloud storage service.

It allows browser-based file access, uploads, and downloads.

Nextcloud demonstrates:

- Self-hosted cloud storage
- Web application deployment
- Database-backed Docker service
- Reverse proxy routing

---

## Prometheus

Prometheus collects metrics from configured targets.

In this project, Prometheus collects metrics from:

- Prometheus itself
- Node Exporter
- cAdvisor

Prometheus stores time-series data so the server can be monitored over time.

---

## Grafana

Grafana displays the data collected by Prometheus.

Grafana dashboards make it easier to view:

- CPU usage
- RAM usage
- Disk usage
- Container usage
- Service status
- Historical trends

---

## Node Exporter

Node Exporter exposes host-level server metrics.

Examples include:

- CPU usage
- Memory usage
- Disk usage
- Filesystem metrics
- System metrics

---

## cAdvisor

cAdvisor exposes Docker container metrics.

Examples include:

- Container CPU usage
- Container memory usage
- Active containers
- Container resource behavior

---

## Raspberry Pi

The Raspberry Pi is used as a physical status display.

It connects the software system to hardware output.

The Pi can check server status and display results using LEDs.

---

## Related Monitoring Extension

A separate repository exists for machine learning and monitoring experiments:

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

That repository is related to the monitoring stack, but this CSC 494 repository focuses on the smart media server infrastructure.
