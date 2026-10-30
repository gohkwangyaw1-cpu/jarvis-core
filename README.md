# JARVIS CORE

> **3D Embodied AI Productivity Assistant with Google Gemini & Three.js**

[![Three.js](https://img.shields.io/badge/Three.js-r128-black?style=for-the-badge&logo=three.js)](https://threejs.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-Flash--Lite-blue?style=for-the-badge&logo=google)](https://ai.google.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Security Audited](https://img.shields.io/badge/Security-Cloudflare_Hardened-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)](#keamanan-sistem--hardening)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg?style=for-the-badge)](LICENSE)

---

## Ikhtisar Proyek

**JARVIS CORE** adalah aplikasi asisten produktivitas modern berbasis web yang memadukan kecerdasan bahasa Google Gemini (`gemini-flash-lite-latest`) dengan entitas visual 3D hidup (*embodied AI*) yang berdenyut dan berinteraksi secara real-time menggunakan Three.js r128. 

Mengusung tata letak spasial **Spatial 3-Column Glassmorphism**, Jarvis Core menyajikan pengalaman kerja bebas distraksi: pengguna dapat mencatat tugas, menandai pekerjaan selesai, memicu timer fokus Pomodoro, dan berdiskusi melalui percakapan alami, didukung oleh respons emosi dinamis dan modulasi vokal berkarakter khas Pak Jokowi.

Aplikasi ini mengadopsi arsitektur **Zero-Build Single-File Architecture**: seluruh logika front-end, visual 3D, state machine, dan speech synthesis terangkum rapi dalam satu berkas `index.html` tanpa memerlukan instalasi Node.js, npm, webpack, atau bundler rumit.

---

## Arsitektur Tata Letak Spasial (Spatial 3-Column)

Antarmuka dirancang dengan sistem koordinat tetap (*Fixed Spatial Positioning*) untuk menjamin **Zero Layout Shift**: kanvas 3D di tengah dan panel tugas di kanan tidak akan bergeser sedikit pun saat riwayat obrolan memanjang.

```
+---------------------------------------------------------------------------------+
|                               JARVIS CORE SPATIAL UI                            |
+---------------------------------------------------------------------------------+
|  [PANEL KIRI]               [AREA TENGAH]                    [PANEL KANAN]      |
|  Riwayat Chat Melayang      Kanvas 3D Terapung               Panel Produktivitas|
|  - Balon pesan kaca         - THREE.IcosahedronGeometry      - Mini Pomodoro    |
|  - Aliran atas ke bawah     - Vertex Wave Morphing             Timer (Preset &  |
|  - Badge status emosi       - Dynamic Spatial Orbit Rings      Progress Bar)    |
|  - Label aksi tugas/timer   - Scale-in Bloom Animation       - Smart To-Do List |
|                             - Mouse Drag Orbit Controls        (Counter & CRUD) |
|                                                                                 |
|                      +-------------------------------+                          |
|                      |   [DOCK INPUT TENGAH BAWAH]   |                          |
|                      |  Input Teks + Voice Over Mute |                          |
|                      +-------------------------------+                          |
+---------------------------------------------------------------------------------+
```

---

## Fitur Unggulan

### 1. Center-Stage 3D Embodied AI Core
- **Geometri Fisik:** Menggunakan `THREE.IcosahedronGeometry` dengan material fisik kaca reflektif (`MeshPhysicalMaterial`) serta kawat kisi orbital (`MeshBasicMaterial`).
- **Vertex Wave Morphing:** Setiap puncak simpul geometris berosilasi mengikuti gelombang sinus dinamis, merefleksikan tingkat distorsi dan ketegangan emosi AI.
- **Dua Cincin Orbit Mandiri:** Cincin spasial ganda (`THREE.TorusGeometry`) berotasi independen mengitari inti 3D.
- **Animasi Scale-in Bloom:** Objek 3D mekar secara halus dari titik nol saat inisialisasi aplikasi selesai, menciptakan transisi visual yang elegan.
- **Interaksi Sentuh & Geser:** Pengguna dapat memutar sudut pandang inti 3D secara bebas menggunakan klik atau sentuhan mouse.

### 2. Autonomous Dynamic Persona & Emotion Engine
Jarvis Core tidak menggunakan dropdown persona manual yang kaku. Model kecerdasan buatan secara otonom menganalisis nada emosi percakapan pengguna dan beradaptasi secara instan:
- **Tenang & Fokus (Calm):** Warna biru indigo (`#4F46E5`), rotasi lambat (0.006), distorsi minim (0.03). Nada bicara terstruktur dan hemat kata.
- **Hangat & Suportif (Friendly):** Warna hijau emerald (`#10B981`), rotasi sedang (0.012), distorsi 0.07. Memberikan semangat hangat layaknya rekan kerja.
- **Mentor Tegas (Strict):** Warna merah menyala (`#EF4444`), rotasi cepat (0.035), distorsi berduri tajam (0.20). Aktif jika pengguna menunda tugas atau malas, memberikan teguran berwibawa khas Pak Jokowi: *"Lho lho lho, kok malah mau rebahan main game? Tugasnya ini lho numpuk, saya titip diselesaikan dulu ya. Bekerja, bekerja, bekerja!"*.
- **Visioner Liar (Wild):** Warna ungu elektrik (`#9333EA`), rotasi kinetik (0.024), distorsi tinggi (0.15). Menghasilkan ide-ide inovatif dan terobosan masa depan.

### 3. Voice Over Berkarakter Suara Pak Jokowi
- **Modulasi Akustik Khusus:** Parameter Web Speech API disetel presisi (Pitch: 0.76, Rate: 0.86) untuk menangkap frekuensi bariton santai, serak-basah, dan tempo tutur berjarak khas Pak Jokowi dari Solo.
- **Prioritas Vokal Alami:** Sistem otomatis mendeteksi dan memilih profil vokal pria Jawa/Indonesia (`jv-ID-DimasNeural`, `id-ID-ArdiNeural`, atau suara pria lokal sistem) jika tersedia di perangkat klien.
- **Speech Fluctuation Synchronizer:** Nilai parameter temperature pada bilah kontrol ikut berosilasi dinamis saat vokal AI berbicara, memberikan umpan balik visual bahwa asisten sedang bertutur kata.

### 4. Synthesizer Audio Taktil & Chime Bel (Web Audio API)
- **Crystal Chime Alarm:** Saat timer Pomodoro menyentuh 00:00, synthesizer Web Audio API membunyikan 3 nada harmonis kristal (D5: 587Hz, A5: 880Hz, D6: 1174Hz) tanpa memerlukan file aset audio eksternal.
- **Peringatan Suara Otomatis:** Begitu bel berdering, Jarvis langsung mengingatkan: *"Waktu fokus sudah selesai ya... Silakan istirahat sebentar, renggangkan badan, nanti kita gas lagi ya."*.
- **Tactile Click Feedback:** Suara klik mekanis halus saat menekan tombol Mulai, Jeda, atau Reset.

### 5. Otomasi Produktivitas Lengkap via Chat
Pengguna dapat mengendalikan seluruh sistem produktivitas hanya dengan mengetik perintah alami di kolom chat:
- **Tambah Tugas:** *"Catat tugas siapkan proposal teknis"* -> Otomatis masuk ke daftar tugas.
- **Selesaikan Tugas:** *"Tandai tugas proposal sudah selesai"* -> Otomatis tercentang dan dicoret.
- **Hapus Tugas:** *"Hapus tugas beli kopi"* -> Item dihapus dari daftar.
- **Kontrol Timer:**
  - *"Pasang timer 20 menit"* -> Timer langsung berjalan 20:00.
  - *"Jeda timer"* -> Timer berhenti sementara.
  - *"Lanjutkan timer"* -> Timer kembali berhitung mundur.
  - *"Reset timer"* -> Timer kembali ke setelan default 25:00.

### 6. Dual-Mode Intelligence (Online Gemini & Offline Fallback)
- **Online Tier Flash-Lite:** Terhubung ke endpoint resmi Google Gemini `gemini-flash-lite-latest` (dan fallback `gemini-3.5-flash-lite`) dengan skema JSON terstruktur, menghasilkan latensi sub-detik (0.8s) yang sangat hemat kuota token.
- **Intelligent Offline Fallback:** Jika jaringan internet terputus atau kunci API belum dimasukkan, sistem secara cerdas beralih ke engine regex lokal. Seluruh manipulasi 3D, pengelolaan tugas, timer, dan voice over tetap berjalan mulus tanpa error.

---

## Keamanan Sistem & Hardening

Proyek ini telah melalui audit keamanan sistem berbasis standar **Cloudflare Security Audit** dengan hasil pengerasan pertahanan mendalam:

| Lapisan Keamanan | Implementasi & Proteksi |
| :--- | :--- |
| **Content Security Policy (CSP)** | `default-src 'self'`. Pembatasan koneksi keluar (`connect-src`) hanya diizinkan ke origin lokal dan endpoint resmi Google Gemini (`generativelanguage.googleapis.com`). Mencegah eksfiltrasi data tanpa izin. |
| **Anti-Clickjacking** | Header `X-Frame-Options: SAMEORIGIN` mencegah aplikasi dibungkus oleh iframe jahat di domain luar. |
| **Anti-MIME Sniffing** | Header `X-Content-Type-Options: nosniff` memblokir eksploitasi manipulasi tipe konten browser. |
| **Referrer & Permissions** | Header `Referrer-Policy: strict-origin-when-cross-origin` dan pembatasan izin perangkat luar (`camera=(), geolocation=()`). |
| **Penyembunyian Server** | Parameter Nginx `server_tokens off;` memangkas banner versi server HTTP untuk mencegah pemindaian otomatis penyerang. |
| **Isolasi Kredensial** | Kunci API Gemini disimpan lokal di `localStorage` peramban klien dan tidak pernah disematkan secara terbuka di riwayat commit publik. |
| **Sanitasi XSS Berlapis** | Seluruh masukan teks, label metadata, dan kode warna heksadesimal wajib melewati escaping HTML ketat dan validasi regex (`^#[0-9A-Fa-f]{6}$`). |

---

## Panduan Instalasi & Menjalankan Aplikasi

Pilih salah satu cara termudah berikut untuk menjalankan Jarvis Core di lingkungan lokal atau server Anda:

### Opsi 1: Docker Compose (Direkomendasikan)
Clone repositori dan jalankan container Nginx yang telah diperkeras dengan satu perintah:

```bash
git clone https://github.com/gohkwangyaw1-cpu/jarvis-core.git
cd jarvis-core
docker compose up -d
```

Aplikasi langsung dapat diakses di browser pada:
`http://localhost:8502`

### Opsi 2: Docker CLI Mandiri
```bash
docker build -t jarvis-core .
docker run -d --name jarvis-core -p 8502:80 --restart unless-stopped jarvis-core
```

### Opsi 3: Python Web Server (Tanpa Docker / Zero-Build)
Karena tidak membutuhkan build step atau dependensi node_modules, Anda dapat langsung menyajikannya menggunakan server HTTP Python bawaan:

```bash
cd jarvis-core
python3 -m http.server 8502
```

Kunjungi `http://localhost:8502` pada peramban web Anda.

---

## Skema JSON Output Gemini

Model Google Gemini diprogram secara ketat untuk mengembalikan respon dalam skema JSON berikut:

```json
{
  "reply": "Pesan tutur asisten kepada pengguna",
  "moodLabel": "Status emosi (Fokus, Ramah, Tegas, Kreatif)",
  "colorHex": "#4F46E5",
  "rotationSpeed": 0.006,
  "distortion": 0.03,
  "detectedPersona": "calm",
  "newTodo": "Judul tugas baru (kosongkan jika tidak ada)",
  "completeTodo": "Judul tugas yang diselesaikan",
  "deleteTodo": "Judul tugas yang dihapus",
  "clearCompleted": false,
  "timerAction": "none",
  "setTimerMinutes": 0
}
```

---

## Struktur Berkas Repositori

```
jarvis-core/
├── .gitignore              # Mengabaikan cache, temporary scratch, dan log
├── Dockerfile              # Container image Nginx Alpine dengan pengerasan keamanan
├── docker-compose.yml      # Orkestrasi container port 8502
├── index.html              # Aplikasi web utama Three.js r128 spasial 3D mandiri
├── nginx-hardened.conf     # Konfigurasi Nginx Cloudflare security headers & server_tokens off
├── RANCANGAN_PROYEK.md     # Blueprint arsitektur teknis dan spesifikasi sistem mendalam
├── README.md               # Dokumentasi resmi proyek
└── test_jarvis.py          # Test suite otomatis (10/10 Unit Tests PASS, Zero Em-Dash)
```

---

## Pengujian Kualitas & Unit Testing

Proyek ini dilengkapi dengan suite pengujian otomatis Python (`unittest`) yang memverifikasi integritas antarmuka, parsing skema, keamanan CSP, dan kepatuhan Zero Em-Dash.

Jalankan pengujian menggunakan interpreter Python:

```bash
python3 test_jarvis.py -v
```

Hasil uji:
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

## Lisensi & Kontribusi

Proyek ini dirilis di bawah lisensi terbuka [MIT License](LICENSE).
Kontribusi, pembukaan isu (*issues*), dan pengajuan *pull request* sangat disambut baik untuk pengembangan Jarvis Core ke depannya.

Dibuat dengan dedikasi untuk produktivitas fokus dan antarmuka spasial masa depan.
