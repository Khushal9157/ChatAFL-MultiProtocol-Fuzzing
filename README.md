# ChatAFL State-Aware Stateful Protocol Fuzzing

## Overview

This repository contains the reproduction and extension of the ChatAFL research work for stateful network protocol fuzzing using AFLNet and Docker-based execution environments.

The project reproduces benchmark stateful fuzzing experiments on multiple protocol targets and proposes a novel state-aware prompting methodology for improving LLM-guided protocol fuzzing.

---

# Objectives

The project focuses on:

1. Reproducing ChatAFL benchmark experiments
2. Performing protocol-aware stateful fuzzing using AFLNet
3. Evaluating fuzzing behavior on RTSP, FTP, and HTTP servers
4. Proposing a state-aware dynamic prompting methodology

---

# Environment

## Platform
- Windows 11
- WSL2 Ubuntu 22.04
- Docker

## Tools
- AFLNet
- ChatAFL
- Docker
- gcov
- gcovr

---

# Repository Structure

```text
report/
│
├── Final_ChatAFL_Report.docx

patches/
│
├── state_aware_prompting_extension.py

README.md
```

---

# Protocol Targets

| Protocol | Target Server |
|----------|---------------|
| RTSP | Live555 |
| FTP | LightFTP |
| HTTP | Lighttpd |

---

# Reproduction Setup

## RTSP - Live555

### Build Docker Image

```bash
docker build . -t live555
```

### Run Container

```bash
docker run -it --rm live555 bash
```

### Run AFLNet

```bash
cd experiments

./run aflnet out "-P RTSP -D 10000 -q 3 -s 3 -E -K -R -m none" 300 5
```

---

## FTP - LightFTP

### Build Docker Image

```bash
docker build . -t lightftp
```

### Run Container

```bash
docker run -it --rm lightftp bash
```

### Run AFLNet

```bash
cd experiments

./run aflnet out "-P FTP -D 10000 -q 3 -s 3 -E -K -R -m none" 300 5
```

---

## HTTP - Lighttpd

### Build Docker Image

```bash
docker build . -t lighttpd
```

### Run Container

```bash
docker run -it --rm lighttpd bash
```

### Run AFLNet

```bash
cd experiments

./run aflnet out "-P HTTP -D 10000 -q 3 -s 3 -E -K -R -m none" 300 5
```

---

# Proposed Novel Work

## State-Aware Dynamic Prompting

The original ChatAFL framework primarily relies on static prompting strategies using predefined protocol templates.

This project proposes a state-aware dynamic prompting methodology where prompts are dynamically adapted based on:
- protocol state transitions
- server response behavior
- previously explored states
- coverage feedback

The proposed methodology aims to improve:
- protocol-state exploration
- semantic validity of generated messages
- adaptive protocol interaction
- fuzzing efficiency

The state-aware dynamic prompting extension is implemented in:

```text
patches/state_aware_prompting_extension.py
```

The implementation introduces adaptive prompt generation using protocol-state tracking, response-aware prompt adaptation, and coverage-guided context generation for stateful protocol fuzzing.

---

# Report

The detailed implementation, reproduction analysis, experimental comparison, and novelty evaluation are available in:

```text
report/Final_ChatAFL_Report.docx
```

---

# References

## Original Paper

https://mboehme.github.io/paper/NDSS24-chatafl.pdf

## Original ChatAFL Repository

https://github.com/ChatAFLndss/ChatAFL

# Authors

Project developed for Stateful Protocol Fuzzing Reproduction and Extension Study.