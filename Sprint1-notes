Sprint 1 – Infrastructure Setup & Core Services Deployment

Project: AI-Driven Smart Home Media Server
Server Name: arnzenmediaserver
Date: March 2026
Environment: Ubuntu Server 24.04.4 LTS

Objective of Sprint 1
The goal of Sprint 1 was to:
- Deploy the Ubuntu server environment
- Install Docker & Docker Compose
- Deploy core containerized services
- Configure networking and DNS
- Establish secure external access using Cloudflare Tunnel
- Validate local and external connectivity
- Identify and resolve initial deployment issues

Server Environment
Operating System: Ubuntu 24.04.4 LTS (Noble)
Kernel: Up to date
Hostname: arnzenmediaserver

Local Network Configuration
Server: Local IP	192.168.1.11
Router: Netgear R7000
Gateway: 192.168.1.1
LAN Subnet: 192.168.1.0/24

Static IP was configured at the router level.
Public Network Information
Public IP (at time of testing)
curl -4 ifconfig.me

Returned:
131.241.xxx.xxx


Docker Environment Setup
Installed Components:
- Docker Engine
- Docker Compose (v2 plugin)
- cloudflared

Verified with:
docker --version
- docker compose version
- cloudflared --version

Core Services Deployed (Sprint 1 Scope)
Services deployed via Docker Compose:
- MariaDB (10.11)
- Redis (alpine)
- Nextcloud (latest)
- Plex (separate container)
- Nginx Proxy Manager (already existing network npm_default)

Docker Compose Configuration
Location:
/data/docker/nextcloud/compose.yml
Key architecture decisions:
All services attached to npm_default network
Persistent volumes mapped to /data/nextcloud/
Port 8080 mapped to container port 80 for Nextcloud
Environment variables set for DB connectivity

Verified services running:
docker ps
Output confirmed:
nextcloud-app
nextcloud-db
nextcloud-redis

Local Service Validation
Test: Nextcloud reachable locally
curl -I http://127.0.0.1:8080

Response:
HTTP/1.1 200 OK
Server: Apache/2.4.66 (Debian)
X-Powered-By: PHP/8.4.18

Confirms:

Apache running
PHP working
Database connectivity functional
Container networking functional



Proxy status:
Initially Proxied 
Later switched to DNS only (grey cloud) for testing
Router Port Forwarding Configured
Netgear R7000:
Service	External Port	Internal IP	Internal Port
HTTP	80	192.168.1.11	80
HTTPS	443	192.168.1.11	443
Plex	32400	192.168.1.11	32400

Issue Encountered – Cloudflare Error 522
When accessing:
https://cloud.arnzenserver.org
Received:
Error 522 – Connection Timed Out
Diagnosis:
Browser: Working
Cloudflare: Working
Host: Not responding
Conclusion:
Cloudflare could not reach origin server.

Root Cause Analysis
Public IP mismatch
Possible ISP-level NAT
Port forwarding unreliable
Potential ISP port blocking
CG-NAT likely in use
Result:
Direct port-forwarding solution deemed unreliable.

Architectural Decision Change
Instead of:
Exposing ports 80/443
Relying on public IP stability
We implemented:

Cloudflare Tunnel (Zero Trust Architecture)
Cloudflare Tunnel Setup
Installed:
sudo apt install cloudflared
Logged in:
cloudflared tunnel login
Created tunnel:
cloudflared tunnel create homelab
Tunnel ID:
43a806e2-e6b9-4092-972c-a3774a479396

DNS Routing to Tunnel
Executed:
cloudflared tunnel route dns homelab cloud.arnzenserver.org
cloudflared tunnel route dns homelab media.arnzenserver.org

CNAME records created automatically pointing to tunnel.
This removed dependency on:
Public IP
Router port forwarding
ISP restrictions

Cloudflared Configuration
File:
~/.cloudflared/config.yml
Ingress routing:
cloud.arnzenserver.org → 127.0.0.1:8080
media.arnzenserver.org → 127.0.0.1:32400
This allows:
Secure outbound-only connection from server → Cloudflare → Users
No inbound ports exposed.

Issues Encountered During Sprint 1
YAML Formatting Errors
Errors:
services.ports must be a mapping
services.restart must be a mapping
Cause:
Incorrect indentation and YAML structure.

Resolution:
Rewrote compose.yml with correct list formatting and proper network declarations.
Docker Compose Warning
version attribute is obsolete

Harmless in Compose v2.
DNS Conflict Errors
Error:
Failed to create record ... A record already exists
Resolution:
Removed conflicting A records before creating tunnel CNAME routes.

Security Improvements Achieved
Sprint 1 ended with:
No open inbound ports required
Encrypted HTTPS via Cloudflare
Internal services only bound locally
Persistent storage for database and files
Segmented Docker network

Sprint 1 Success Criteria – Status
Item	Status
Ubuntu server installed	✅
Docker installed	✅
Core services deployed	✅
Local service connectivity verified	✅
DNS configured	✅
Cloudflare tunnel established	✅
- Plex not available externally
522 error resolved via architecture change	✅
Sprint 1 Conclusion

Sprint 1 successfully established:
A containerized home server infrastructure
Secure external routing using Cloudflare Tunnel
Persistent storage and database services
A functional Nextcloud instance locally verified
A production-ready architecture avoiding ISP NAT limitations

The system is now ready for:
Sprint 2: 
Plex connectivity for external use
shared mounted location for nextcloud and plex to upload files directly to plex
dvd ripper
Monitoring & Observability (Prometheus, Grafana)
AI-driven predictive workload monitoring
Attach hardware displays to track disk,cpu, and other monitoring tools 
Performance analytics
