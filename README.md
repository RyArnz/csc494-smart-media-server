# CSC 494 Smart Home Media Server

## Project Summary
This project builds a self-hosted smart home media and cloud platform on Ubuntu Server using Docker. The system provides remote media streaming through Plex, public cloud storage through Nextcloud, and live monitoring through Prometheus and Grafana. A Raspberry Pi extends the project into an IoT-style status display that reflects server health through physical indicators.

## Problem
Home users often rely on separate commercial services for media streaming, file storage, and system monitoring. This project solves that by building a centralized self-hosted platform that provides media access, cloud storage, and observability from one server.

## Why This Problem Matters
A self-hosted platform gives the user more control over data, services, and uptime. It also demonstrates practical skills in Linux administration, Docker deployment, networking, reverse proxy configuration, monitoring, and hardware integration.

## Solution
The solution is an Ubuntu Server host running Dockerized services for Plex, Nextcloud, Nginx Proxy Manager, Prometheus, Grafana, node_exporter, and cAdvisor. Plex provides local and remote media access, Nextcloud provides domain-based cloud storage, and Prometheus/Grafana provide live host and container monitoring. A Raspberry Pi polls server metrics and drives an LED status panel.

## Technology Stack
- Ubuntu Server
- Docker / Docker Compose
- Plex
- Nextcloud
- Nginx Proxy Manager
- Prometheus
- Grafana
- node_exporter
- cAdvisor
- Raspberry Pi 4
- Python 3
- gpiozero

## Architecture
[insert architecture diagram image here]

## Services
- Plex: local + remote media streaming
- Nextcloud: public domain cloud storage
- Nginx Proxy Manager: reverse proxy / HTTPS management
- Prometheus: metrics collection
- Grafana: dashboard visualization
- node_exporter: host metrics
- cAdvisor: container metrics
- Raspberry Pi: hardware telemetry endpoint

## Validation Results
- Plex local access verified
- Plex remote access verified
- Nextcloud public domain verified
- Prometheus targets verified UP
- Grafana node and container dashboards verified working
- Raspberry Pi LED integration in progress / completed

## Screenshots
[insert screenshots]

## Demo Video
[insert video link]

## Final Presentation PDF
[insert Marp PDF link]

## Future Improvements
- LCD or OLED hardware display
- Tautulli integration for active Plex sessions
- MQTT event layer
- alerting and notifications
