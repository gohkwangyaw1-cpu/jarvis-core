# JARVIS CORE

> **3D Embodied AI Productivity Assistant powered by Google Gemini & Three.js**

[![Three.js](https://img.shields.io/badge/Three.js-r128-black?style=for-the-badge&logo=three.js)](https://threejs.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Flash--Lite-blue?style=for-the-badge&logo=google)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Security Audited](https://img.shields.io/badge/Security-Cloudflare_Hardened-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)](#system-security--hardening)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg?style=for-the-badge)](LICENSE)

---

## Executive Overview

**JARVIS CORE** is a next-generation web-based AI productivity workspace combining Google Gemini's high-speed multimodal reasoning (`gemini-flash-lite-latest`) with a living, real-time 3D embodied visual entity powered by Three.js r128.

Engineered with a **Spatial 3-Column Glassmorphism Layout**, Jarvis Core delivers a clutter-free, distraction-resistant focus cockpit: users can organize task lists, complete milestones, trigger Pomodoro focus countdowns, and brainstorm through natural dialogue, supported by real-time emotion recognition and acoustic voice synthesis.

Built upon a **Zero-Build Single-File Architecture**, the complete front-end logic, 3D vertex shaders, reactive state machine, and audio synthesis run directly in the browser via standalone `index.html` without requiring Node.js, npm packages, or bundlers.

---

## Spatial UI Architecture (Spatial 3-Column)

The interface utilizes **Fixed Spatial Positioning** coordinates to eliminate layout shift: the 3D center stage and productivity widgets remain locked in position as chat dialogues expand.

```
+---------------------------------------------------------------------------------+
|                               JARVIS CORE SPATIAL UI                            |
+---------------------------------------------------------------------------------+
|  [LEFT PANEL]               [CENTER STAGE]                   [RIGHT PANEL]      |
|  Floating Chat Stream       Floating 3D Orb Canvas           Productivity Panel |
|  - Glass bubble stream      - THREE.IcosahedronGeometry      - Integrated Mini  |
|  - Top-to-bottom flow       - Vertex Wave Morphing             Pomodoro Timer   |
|  - Real-time mood badges    - Dynamic Spatial Orbit Rings      (Preset & Bar)   |
|  - Task & timer tags        - Scale-in Bloom Animation       - Smart To-Do List |
|                             - Mouse Drag Orbit Controls        (Counter & CRUD) |
|                                                                                 |
|                      +-------------------------------+                          |
|                      |  [BOTTOM CENTER FLOATING DOCK]|                          |
|                      |  Input Bar + Voice Over Mute  |                          |
|                      +-------------------------------+                          |
+---------------------------------------------------------------------------------+
```

---

## Key Features

### 1. Center-Stage 3D Embodied AI Core
- **Physical Geometry:** Constructed with `THREE.IcosahedronGeometry` utilizing glass reflective physics (`MeshPhysicalMaterial`) paired with orbital wireframe meshes (`MeshBasicMaterial`).
- **Vertex Wave Morphing:** Real-time mathematical vertex displacement driven by dynamic noise sine functions, pulsating to reflect the assistant's cognitive distortion and focus states.
- **Dual Autonomous Orbit Rings:** Spatial dual toruses (`THREE.TorusGeometry`) spinning on decoupled axes around the core.
- **Scale-in Bloom Animation:** The 3D orb blooms smoothly into view from scale zero upon application initialization, ensuring seamless visual onboarding.
- **Tactile Drag Controls:** Full 360-degree interactive camera orbit inspection via mouse drag or touch inputs.

### 2. Autonomous Affective Persona & Emotion Engine
Jarvis Core does not use rigid manual dropdown pickers. The AI automatically analyzes the emotional tone and user intent in real-time, morphing its state immediately:
- **Calm & Focus:** Indigo tone (`#4F46E5`), gentle rotation (0.006), minimal distortion (0.03). Delivers structured, concise, and direct focus guidance.
- **Warm & Friendly:** Emerald green (`#10B981`), moderate rotation (0.012), subtle pulse distortion (0.07). Provides supportive, conversational camaraderie.
- **Strict Mentor:** Intense red (`#EF4444`), rapid rotation (0.035), sharp spiky distortion (0.20). Automatically triggers when the user procrastinates or expresses laziness, offering authoritative reminders to return to deep work.
- **Wild Visionary:** Electric purple (`#9333EA`), kinetic rotation (0.024), high organic wave distortion (0.15). Stimulates creative breakthroughs and lateral thinking.

### 3. Voice Synthesis & Acoustic Modulation
- **Precision Timbre Modulation:** Web Speech API parameters calibrated (Pitch: 0.76, Rate: 0.86) to render a calm, authoritative, and relaxed baritone cadence.
- **Adaptive Voice Discovery:** Prioritizes natural neural Indonesian and Javanese male voices (`jv-ID-DimasNeural`, `id-ID-ArdiNeural`, or native system male synthesizers) across supported client browsers.
- **Speech Oscillation Synchronizer:** The temperature readout dynamically oscillates while speech is active, providing intuitive visual feedback that the agent is actively talking.

### 4. Tactile Audio Synthesizer & Chime (Web Audio API)
- **Harmonic Crystal Chime:** When the countdown reaches 00:00, the Web Audio API generates a crystal chime (D5: 587Hz, A5: 880Hz, D6: 1174Hz) without loading external audio assets.
- **Automated Spoken Notification:** Following the chime, Jarvis delivers an immediate voice reminder that the focus block is complete.
- **Tactile Click Feedback:** Soft mechanical audio clicks accompany button presses on Start, Pause, and Reset controls.

### 5. Chat-Driven Productivity Automation
Control the entire workspace using plain conversational language:
- **Task Addition:** *"Add task prepare quarterly budget"* -> Instantly appended to the checklist.
- **Task Completion:** *"Mark task quarterly budget as done"* -> Checked off and strikethrough applied.
- **Task Deletion:** *"Delete task buy coffee"* -> Removed from the list.
- **Timer Management:**
  - *"Set focus timer for 20 minutes"* -> Timer starts counting down from 20:00.
  - *"Pause timer"* -> Timer pauses immediately.
  - *"Resume timer"* -> Countdown resumes.
  - *"Reset timer"* -> Restores default 25:00 focus block.

### 6. Dual-Mode Cognitive Pipeline (Online Gemini & Offline Fallback)
- **High-Throughput Gemini Flash-Lite:** Powered by Google's official `gemini-flash-lite-latest` (with fallback to `gemini-3.5-flash-lite`) via Structured JSON outputs, delivering sub-second responses with minimal token overhead.
- **Intelligent Local Fallback:** In the event of network disruption or missing API keys, an internal regex cognitive fallback seamlessly handles task parsing, timer commands, and conversational dialogue with zero disruption or error screens.

---

## System Security & Hardening

Jarvis Core adheres to **Cloudflare Security Audit Standards** with defense-in-depth measures implemented across both client and server layers:

| Security Vector | Implementation & Defensive Protection |
| :--- | :--- |
| **Content Security Policy (CSP)** | `default-src 'self'`. Outbound connections (`connect-src`) strictly restricted to local origins and Google Gemini's official API (`generativelanguage.googleapis.com`). Blocks data exfiltration. |
| **Anti-Clickjacking** | `X-Frame-Options: SAMEORIGIN` prevents unauthorized third-party iframe framing and UI redressing attacks. |
| **Anti-MIME Sniffing** | `X-Content-Type-Options: nosniff` defends against MIME-confusion exploits. |
| **Referrer & Permissions** | `Referrer-Policy: strict-origin-when-cross-origin` and lockdown on unused hardware permissions (`camera=(), geolocation=()`). |
| **Server Token Stripping** | Nginx `server_tokens off;` strips HTTP server version identifiers from response headers. |
| **Credential Isolation** | Gemini API keys are stored locally within client `localStorage` and are excluded from public source code repositories. |
| **Strict XSS Sanitization** | All rendered text, metadata badges, and hex color codes undergo HTML escaping and regex pattern enforcement (`^#[0-9A-Fa-f]{6}$`). |

---

## Deployment & Getting Started

### Option 1: Docker Compose (Recommended)
Clone the repository and deploy the hardened Nginx container with a single command:

```bash
git clone https://github.com/gohkwangyaw1-cpu/jarvis-core.git
cd jarvis-core
docker compose up -d
```

Access the interface in your browser at:
`http://localhost:8502`

### Option 2: Standalone Docker CLI
```bash
docker build -t jarvis-core .
docker run -d --name jarvis-core -p 8502:80 --restart unless-stopped jarvis-core
```

### Option 3: Python Web Server (Zero-Build)
With no build steps or dependencies required, launch directly using Python's standard HTTP server:

```bash
cd jarvis-core
python3 -m http.server 8502
```

Navigate to `http://localhost:8502` in any modern web browser.

---

## Structured Output JSON Schema

The Gemini model is constrained via Google GenAI Structured JSON Schema:

```json
{
  "reply": "Assistant response text",
  "moodLabel": "Current emotional state label (Focus, Friendly, Strict, Creative)",
  "colorHex": "#4F46E5",
  "rotationSpeed": 0.006,
  "distortion": 0.03,
  "detectedPersona": "calm",
  "newTodo": "New task string (empty if none)",
  "completeTodo": "Task string to complete",
  "deleteTodo": "Task string to delete",
  "clearCompleted": false,
  "timerAction": "none",
  "setTimerMinutes": 0
}
```

---

## Repository Structure

```
jarvis-core/
├── .gitignore              # Ignores local caches, scratch files, and logs
├── Dockerfile              # Production Nginx Alpine container image
├── docker-compose.yml      # Container service orchestration for port 8502
├── index.html              # Core single-file Three.js r128 application
├── nginx-hardened.conf     # Hardened Nginx configuration with Cloudflare headers
├── RANCANGAN_PROYEK.md     # In-depth architectural blueprint and technical specifications
├── README.md               # Official project documentation
└── test_jarvis.py          # Automated verification test suite (10/10 Tests PASS)
```

---

## Quality Assurance & Automated Testing

The project includes an automated test suite verifying DOM structure, schema parsing, security headers, and Zero Em-Dash compliance.

Execute the test suite with:

```bash
python3 test_jarvis.py -v
```

Output:
```text
test_all_four_personas_configured ... ok
test_api_key_security_and_storage ... ok
test_dom_elements_present ... ok
test_loading_screen_and_onboarding ... ok
test_required_files_exist ... ok
test_security_headers_and_sanitization ... ok
test_threejs_and_tailwind_cdn ... ok
test_timer_action_in_schema ... ok
test_timer_sound_and_chime ... ok
test_zero_em_dash_compliance ... ok

Ran 10 tests in 0.003s - OK
```

---

## License & Attribution

Distributed under the [MIT License](LICENSE).
Contributions, bug reports, and pull requests are welcomed.

Engineered for deep-focus productivity and next-generation embodied spatial computing.
