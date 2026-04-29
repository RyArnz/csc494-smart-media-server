# Demo Video Notes

## Purpose

The demo video shows the completed smart media server project and explains how the major parts connect.

The video demonstrates the system instead of only repeating the slide deck.

---

## Demo Flow

1. Introduce the project
2. Explain the overall architecture
3. Show Plex
4. Show Nextcloud
5. Explain Nginx Proxy Manager
6. Explain Cloudflare Tunnel
7. Show Prometheus endpoints
8. Show Grafana dashboard
9. Show Raspberry Pi integration
10. Explain the main problems solved
11. End with a final project summary

---

## Opening Script

```text
This project is a self-hosted smart media server built with Ubuntu Server, Docker, Plex, Nextcloud, Nginx Proxy Manager, Cloudflare Tunnel, Prometheus, Grafana, and Raspberry Pi integration.
```

---

## Plex Section

Show the Plex dashboard or media library.

Explain:

```text
Plex is the media server part of the project. It allows media stored on the server to be streamed from other devices.
```

---

## Nextcloud Section

Show the Nextcloud dashboard.

Explain:

```text
Nextcloud is the private cloud storage part of the project. It allows files to be uploaded, downloaded, and accessed remotely through a browser.
```

---

## Cloudflare and Nginx Proxy Manager Section

Explain the traffic path:

```text
Cloudflare DNS -> Cloudflare Tunnel -> Nginx Proxy Manager -> Docker service
```

Explain:

```text
Cloudflare Tunnel allows the server to be reached remotely without traditional router port forwarding. Nginx Proxy Manager routes each domain to the correct internal service.
```

---

## Monitoring Section

Show Prometheus endpoints and Grafana dashboards.

Explain:

```text
Prometheus collects metrics from the server and containers. Grafana displays those metrics in dashboards so the server can be monitored visually.
```

---

## Raspberry Pi Section

Show the Raspberry Pi hardware.

Explain:

```text
The Raspberry Pi acts as a physical server-status display. It can show whether the server is healthy, warning, critical, or unreachable.
```

---

## Problems Solved

Mention these problems:

- Plex worked locally but not remotely
- The media domain originally showed the wrong page
- Grafana needed Prometheus data source and target checks
- Remote access required understanding the full traffic route

---

## Closing Script

```text
The final system demonstrates a working home server that supports media streaming, private cloud storage, secure remote access, server monitoring, and Raspberry Pi hardware status output.
```

---

## Do Not Show

Do not show:

- Passwords
- Private tokens
- Cloudflare tunnel secrets
- Private files
- Private media content
- Sensitive configuration values
