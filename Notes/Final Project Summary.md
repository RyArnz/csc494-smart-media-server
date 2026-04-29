# Final Project Summary

## Project Name

CSC 494 Smart Media Server

---

## Summary

This project built a self-hosted smart media server using Ubuntu Server, Docker, Plex, Nextcloud, Nginx Proxy Manager, Cloudflare Tunnel, Prometheus, Grafana, and Raspberry Pi hardware integration.

The final system demonstrates how a home server can host real services, provide remote access through a domain, monitor system health, and connect to an external hardware device.

---

## Main Accomplishments

The project accomplished the following:

- Set up an Ubuntu-based home server
- Deployed multiple services with Docker
- Created a media server using Plex
- Created a private cloud storage service using Nextcloud
- Configured remote access using Cloudflare Tunnel
- Routed public subdomains through Nginx Proxy Manager
- Added Prometheus for server metrics
- Added Grafana for dashboards
- Connected the project idea to Raspberry Pi hardware output
- Documented the architecture, setup, troubleshooting, and future work

---

## Final System Description

The final system uses Cloudflare to route domain traffic to the home server.

Cloudflare Tunnel forwards traffic to the Ubuntu server without requiring traditional router port forwarding.

Nginx Proxy Manager receives the traffic and routes it to the correct Docker container.

Example:

```text
cloud.arnzenserver.org -> Nextcloud
media.arnzenserver.org -> Plex
```

Prometheus and Grafana monitor the server.

The Raspberry Pi provides the basis for a physical server-status display.

---

## Services Included

## Plex

Plex provides media streaming from the home server.

It allows the server to host movies, music, and other media files.

---

## Nextcloud

Nextcloud provides private cloud storage.

It allows files to be uploaded, downloaded, and accessed through a web browser.

---

## Nginx Proxy Manager

Nginx Proxy Manager routes domain traffic to the correct internal service.

It simplifies access by allowing services to use clean domain names instead of raw ports.

---

## Cloudflare Tunnel

Cloudflare Tunnel provides remote access without traditional router port forwarding.

This was important for safely exposing the services outside the local network.

---

## Prometheus

Prometheus collects server and container metrics.

It stores monitoring data over time.

---

## Grafana

Grafana displays Prometheus metrics in dashboards.

It helps visualize server health.

---

## Raspberry Pi

The Raspberry Pi acts as the physical hardware extension of the server.

It can display server status using LEDs or other output devices.

---

## Important Technical Concepts Learned

This project required learning and applying:

- Linux server management
- Docker containers
- Docker Compose
- Reverse proxy routing
- DNS and subdomains
- Cloudflare Tunnel
- Self-hosted web services
- Server monitoring
- Prometheus metrics
- Grafana dashboards
- Raspberry Pi GPIO concepts
- Troubleshooting networked systems

---

## Major Problem Solved

The biggest technical problem was remote access.

A service can work locally but fail remotely if the routing path is wrong.

The key architecture that solved this was:

```text
Cloudflare -> Cloudflare Tunnel -> Nginx Proxy Manager -> Docker service
```

Once that flow worked, the project services could be accessed by domain.

---

## Current Limitations

The current system has some limitations:

1. Some configuration is specific to the current home server
2. Private secrets and passwords cannot be stored in GitHub
3. Media files are not included in the repository
4. The Raspberry Pi setup may require hardware-specific instructions
5. More screenshots and diagrams should be added
6. Monitoring alerting can be improved
7. Backups and disaster recovery could be documented further

---

## Future Improvements

Future work could include:

- Add more screenshots
- Add a complete architecture diagram
- Add a sanitized Docker Compose example
- Add better backup instructions
- Add Grafana alerting
- Add Raspberry Pi wiring diagrams
- Add a more polished demo video
- Add health-check scripts
- Add optional machine learning monitoring from the separate CSC 426 repo

---

## Final Reflection

This project demonstrates a realistic home server environment.

It is more than a single application because it combines networking, containers, storage, monitoring, remote access, and hardware integration.

The most valuable part of the project was learning how all parts of the system connect together.
