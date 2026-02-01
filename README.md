# Smart Home Media System
CSC 494 – Early Starter Project

---

## Team Members

Ryan Arnzen (Team Lead, Infrastructure & Systems)

This is an individual project. All design, setup, and implementation are completed by me.

---

## Project Description

Smart Home Media System is a self-hosted home server built on Ubuntu Server that centralizes media storage, personal cloud services, and containerized applications using Docker.

The goal is to replace multiple third-party services with one secure, locally controlled system that provides storage, remote access, and expandable infrastructure for monitoring and future smart home integrations.

This project emphasizes hands-on learning of Linux administration, networking, containerization, and server security.

---

## Problem Domain

Many home users rely on separate cloud services for storage and media that:

- cost money over time
- limit privacy and control
- are difficult to customize
- scatter data across platforms

There is a need for a centralized, private, and expandable home server that provides:

- local media access
- personal cloud storage
- secure remote connectivity
- room for future automation and monitoring

---

## Features and Requirements

### Features

- Ubuntu Server host
- Docker-based service deployment
- Nextcloud personal cloud storage
- Centralized media storage
- Secure remote access through Cloudflare proxy
- Domain configuration
- Basic monitoring and system health checks
- Optional media ingestion (DVD → digital files)

### Requirements

- Runs reliably on home hardware
- Secure external access
- Modular and scalable design
- Easy to maintain and expand

---

## Non-Functional Requirements

- Linux-based
- Low resource usage
- Secure by default
- Scalable with Docker containers
- Maintainable and organized

---

## Data Model

Data stored on the system includes:

- media files
- photos and videos
- documents
- backups
- system logs

---

## Architecture

High-level structure:

User Devices  
↓  
Cloudflare Proxy  
↓  
Ubuntu Server  
↓  
Docker Containers (Nextcloud + services)

[Insert architecture diagram here]

---

## Tests

### Acceptance Tests
- Server boots correctly
- Docker services run
- Nextcloud accessible locally
- Remote access works through proxy

### Integration Tests
- Containers communicate properly
- Storage persists across restarts

### E2E Tests
- User connects → logs in → uploads/downloads files successfully

---

## Project Documentation

- Project Plan Presentation (PPP)
- Learning with AI notes
- Setup instructions
- Progress updates

---

## Learning with AI Integration

AI will be used as a learning assistant to help understand:

- Linux server setup
- Docker containerization
- networking and proxy configuration
- security practices
- monitoring concepts

AI supports research and troubleshooting, while all implementation is completed manually by me.

---

## Schedule & Milestones

### Sprint 1
- Install Ubuntu Server
- Configure Docker
- Repository setup

### Sprint 2
- Deploy Nextcloud
- Configure storage
- Setup domain and proxy

### Sprint 3
- Add monitoring tools
- Improve security

### Sprint 4
- Media management features
- Testing and polish

Link: (future project board)
