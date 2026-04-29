# Service Notes

## Overview

This file explains the purpose of each major service used in the smart media server project.

---

## Ubuntu Server

Ubuntu Server is the operating system running on the main server machine.

It hosts Docker and all project services.

The server is responsible for:

- Running containers
- Storing media files
- Storing cloud files
- Hosting monitoring services
- Connecting to Cloudflare Tunnel
- Supporting remote access

---

## Docker

Docker runs applications in containers.

In this project, Docker is used because it keeps services organized and easier to manage.

Docker makes it possible to run Plex, Nextcloud, Prometheus, Grafana, and other services on the same machine without installing each application directly onto the operating system.

---

## Docker Compose

Docker Compose defines and manages groups of containers.

It allows services to be started with:

```bash
docker compose up -d
```

It allows services to be stopped with:

```bash
docker compose down
```

Docker Compose is useful because many project services require volumes, ports, networks, and environment variables.

---

## Plex

Plex is the media server.

It organizes and streams media files from the server.

Plex is used for:

- Movies
- Music
- TV shows
- Other media files

Plex demonstrates that the server can host a real media service.

---

## Nextcloud

Nextcloud is the private cloud storage service.

It allows files to be uploaded, downloaded, and managed through a web browser.

Nextcloud is used for:

- Private file storage
- Remote file access
- Browser-based uploads and downloads
- Demonstrating a self-hosted cloud application

---

## MariaDB

MariaDB is the database used by Nextcloud.

Nextcloud needs a database to store information about users, files, settings, and application state.

---

## Redis

Redis is used as a cache or support service for Nextcloud.

It can improve performance and help with file locking or caching depending on the configuration.

---

## Nginx Proxy Manager

Nginx Proxy Manager is the reverse proxy.

It routes domain traffic to the correct internal service.

Example:

```text
cloud.arnzenserver.org -> Nextcloud
media.arnzenserver.org -> Plex
```

Nginx Proxy Manager also provides a web interface for managing proxy hosts.

---

## Cloudflare Tunnel

Cloudflare Tunnel provides remote access without traditional router port forwarding.

Instead of opening ports on the router, the server connects outward to Cloudflare.

Cloudflare then forwards domain traffic through the tunnel to the server.

---

## Cloudflare DNS

Cloudflare DNS manages the project domain and subdomains.

Example subdomains:

```text
cloud.arnzenserver.org
media.arnzenserver.org
```

DNS connects the domain names to the Cloudflare Tunnel and routing setup.

---

## Prometheus

Prometheus collects time-series metrics.

It is used to monitor the health of the server and containers.

Prometheus can collect metrics such as:

- CPU usage
- RAM usage
- Disk usage
- Container CPU usage
- Container memory usage
- Service status

---

## Grafana

Grafana displays Prometheus metrics in dashboards.

Grafana helps visualize the system instead of only reading command-line output.

It can show:

- CPU graphs
- Memory graphs
- Disk graphs
- Container graphs
- Historical trends

---

## Node Exporter

Node Exporter provides host machine metrics to Prometheus.

It exposes information about:

- CPU
- Memory
- Disk
- Filesystems
- System load
- Network-related system data

---

## cAdvisor

cAdvisor provides Docker container metrics to Prometheus.

It exposes information about:

- Container CPU usage
- Container memory usage
- Container count
- Container resource behavior

---

## Raspberry Pi

The Raspberry Pi is used as a hardware extension of the server.

It can check server status and display the result physically using LEDs.

The Raspberry Pi helps connect the project to IoT concepts.

---

## Related Monitoring Repository

The separate monitoring repository is:

```text
https://github.com/RyArnz/csc426-smart-media-ml-monitoring
```

That repository focuses more on machine learning and Prometheus data analysis.

This repository focuses on the smart media server system itself.
