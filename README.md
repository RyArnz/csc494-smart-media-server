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
<img width="1332" height="793" alt="Plex Dashboard" src="https://github.com/user-attachments/assets/215c9b75-478f-4bfe-981f-7ae6b3aef626" />

<img width="1440" height="900" alt="Nextcloud Dashboard" src="https://github.com/user-attachments/assets/8d96532a-2322-4dd8-bfa5-bc48d2cdddd4" />


## Demo Video
[[Demo Video]](https://youtube.com/shorts/-h2SgqsmxSU?feature=share)

## Final Presentation PDF
[[Final Presentation PDF]](https://github.com/RyArnz/csc494-smart-media-server/blob/main/Slides/FinalPresentation.pdf)

## Future Improvements
- extend Raspberry Pi from LEDs to LCD/OLED display 
- add alerts/notifications 
- expand monitoring into predictive maintenance 
- potentially connect with the separate ML monitoring project later


