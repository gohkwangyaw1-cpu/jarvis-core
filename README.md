# Jarvis Core

A lightweight 3D productivity assistant built with Three.js and Google Gemini Flash-Lite. Runs straight out of a single HTML file with no build tools or package managers needed.

[![Three.js](https://img.shields.io/badge/Three.js-r128-black?style=flat-square&logo=three.js)](https://threejs.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Flash--Lite-blue?style=flat-square&logo=google)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg?style=flat-square)](LICENSE)

---

## What It Does

- **Interactive 3D Core:** A Three.js wireframe orb that changes color, spin speed, and surface distortion based on the tone of your chat.
- **Chat-Driven Productivity:** Add tasks, check off completed items, and set Pomodoro timers just by typing naturally (e.g., *"set timer for 20m"*, *"add task review PR"*).
- **Audio Feedback:** Synthesizes voice responses and rings a clean chime when your focus timer hits zero.
- **Zero-Build Architecture:** Everything lives in `index.html`. No `npm install`, no bundlers, no build step.
- **Offline Fallback:** If your API key is missing or offline, the app switches to local regex logic so the 3D core, timer, and to-do list keep working.

---

## Quickstart

### Using Docker Compose (Recommended)

```bash
git clone https://github.com/gohkwangyaw1-cpu/jarvis-core.git
cd jarvis-core
docker compose up -d
```

Open `http://localhost:8502` in your browser.

### Using Python (No Docker)

```bash
cd jarvis-core
python3 -m http.server 8502
```

Then visit `http://localhost:8502`.

---

## API Key Setup

1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Paste it into the setup modal when you first open the app.
3. The key is saved locally in your browser's `localStorage` and is never committed to git or sent anywhere except Google's official Gemini endpoint.

---

## Project Structure

```
jarvis-core/
├── index.html           # Main application (Three.js, UI, and logic in one file)
├── nginx-hardened.conf  # Nginx config with CSP and security headers
├── Dockerfile           # Minimal Nginx Alpine container
├── docker-compose.yml   # Local port 8502 deployment
├── test_jarvis.py       # Automated unit tests
├── RANCANGAN_PROYEK.md  # Original project design notes
└── README.md
```

---

## Running Tests

Run the test suite with Python:

```bash
python3 test_jarvis.py -v
```

---

## License

MIT License. Feel free to use and modify.
