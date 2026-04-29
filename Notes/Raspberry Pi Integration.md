# Raspberry Pi Integration

## Overview

The Raspberry Pi is used as the physical hardware extension of the smart media server project.

The goal is for the Raspberry Pi to receive or request server health information and display that status using hardware output such as LEDs.

---

## Purpose

The Raspberry Pi integration adds an IoT component to the project.

Instead of only viewing server status through a web dashboard, the server can also show its status physically.

This helps connect the smart media server project to hardware, sensors, and real-world feedback.

---

## Basic Concept

The Raspberry Pi checks the server status.

Then it changes LED output based on the result.

Example:

```text
Server healthy       -> Green LED
Moderate warning     -> Yellow LED
Critical issue       -> Red LED
Connection problem   -> Blue LED
```

---

## Possible Data Sources

The Raspberry Pi can get server data from several sources.

## Option 1: Prometheus

The Pi can query Prometheus directly.

Example:

```text
Raspberry Pi -> Prometheus API -> Server metrics
```

This is useful because Prometheus already stores CPU, RAM, disk, and container metrics.

---

## Option 2: Direct Service Checks

The Pi can directly check whether important services are reachable.

Example:

```text
Check Plex URL
Check Nextcloud URL
Check Prometheus URL
Check Grafana URL
```

This is simpler than querying detailed metrics.

---

## Option 3: Custom API

A custom server script could expose a simple status endpoint.

Example:

```text
http://server-ip:5000/status
```

The Pi could read one simplified status result.

---

## Example LED Meanings

```text
Green LED:
The server is reachable and metrics are normal.

Yellow LED:
The server is reachable, but CPU, RAM, or disk usage is elevated.

Red LED:
The server is in a critical state or a major service is down.

Blue LED:
The Raspberry Pi cannot connect to the server or monitoring endpoint.
```

---

## Example Hardware Goal

The Raspberry Pi should eventually support:

- One green LED
- One yellow LED
- One red LED
- One blue LED
- Resistors for each LED
- GPIO output control
- Python script for logic

---

## Example GPIO Planning

Example BCM pins:

```text
Green LED  -> GPIO 17
Blue LED   -> GPIO 27
Yellow LED -> GPIO 19
Red LED    -> GPIO 26
```

The exact pins can be changed as long as the Python script matches the wiring.

---

## Example Logic

```text
If Prometheus cannot be reached:
    Turn on blue LED

Else if disk usage is critical:
    Turn on red LED

Else if CPU or RAM is high:
    Turn on yellow LED

Else:
    Turn on green LED
```

---

## Testing Checklist

- [ ] Raspberry Pi boots
- [ ] Raspberry Pi has network access
- [ ] Python is installed
- [ ] Required Python packages are installed
- [ ] Pi can ping the server
- [ ] Pi can reach Prometheus or selected service URL
- [ ] LEDs are wired correctly
- [ ] GPIO pins match the script
- [ ] Script turns on the correct LED
- [ ] Error state works when the server is unreachable

---

## Useful Commands

Check network:

```bash
ping SERVER_IP
```

Check Prometheus:

```bash
curl http://SERVER_IP:9090/-/ready
```

Run script:

```bash
python3 raspberry_pi_status.py
```

---

## Future Improvements

Future Raspberry Pi improvements could include:

- LCD screen
- OLED display
- Button to cycle status screens
- Buzzer for critical alerts
- More detailed LED patterns
- Case or enclosure
- Automatic startup on boot
- Better logging
