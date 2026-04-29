# Final Presentation Outline

## Slide 1: Project Title

CSC 494 Smart Media Server

Self-hosted media, cloud storage, monitoring, and Raspberry Pi integration.

---

## Slide 2: Project Goal

The goal was to build a working home server that could host real services and be accessed remotely through a secure domain-based setup.

---

## Slide 3: Main Services

- Plex for media streaming
- Nextcloud for private cloud storage
- Nginx Proxy Manager for routing
- Cloudflare Tunnel for remote access
- Prometheus and Grafana for monitoring
- Raspberry Pi for physical status output

---

## Slide 4: Architecture

```text
Cloudflare -> Tunnel -> Nginx Proxy Manager -> Plex / Nextcloud
```

---

## Slide 5: Plex

Plex provides the media server part of the project.

It allows media stored on the server to be streamed from other devices.

---

## Slide 6: Nextcloud

Nextcloud provides private cloud storage.

It allows files to be uploaded, downloaded, and accessed remotely.

---

## Slide 7: Cloudflare Tunnel and Nginx Proxy Manager

Cloudflare Tunnel allows remote access without traditional router port forwarding.

Nginx Proxy Manager routes each domain to the correct internal service.

---

## Slide 8: Monitoring

Prometheus collects server and container metrics.

Grafana displays those metrics in dashboards.

---

## Slide 9: Raspberry Pi Integration

The Raspberry Pi acts as a physical server-status display.

LEDs can show healthy, warning, critical, or connection-error states.

---

## Slide 10: Problems Solved

- Plex worked locally but not remotely
- Media domain showed the wrong page
- Grafana needed correct Prometheus data
- Routing required understanding the full traffic path

---

## Slide 11: What I Learned

I learned how to build and troubleshoot a real server system using Linux, Docker, reverse proxies, Cloudflare Tunnel, monitoring tools, and Raspberry Pi hardware.

---

## Slide 12: Future Work

- Add better diagrams
- Add backups
- Add Grafana alerts
- Improve Raspberry Pi hardware display
- Add health-check scripts
- Optionally connect to the separate AI monitoring project
