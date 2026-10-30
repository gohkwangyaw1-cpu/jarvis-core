# JARVIS CORE - 3D Embodied AI Productivity Assistant

JARVIS CORE adalah antarmuka asisten produktivitas berbasis web yang memadukan model bahasa besar multimodal Google Gemini (Gemini 2.5 Flash dan Gemini 1.5 Flash) dengan visualisasi 3D Center-Stage interaktif berbasis Three.js. Aplikasi ini dirancang menggunakan arsitektur zero-build (tanpa perlu npm install atau bundler), beroperasi langsung melalui satu berkas HTML mandiri (`index.html`), dan mengusung estetika Glassmorphism Light Mode modern.

---

## Fitur Utama

1. **Center-Stage 3D Embodied AI Core:**
   - Bola 3D geometris berbasis `THREE.IcosahedronGeometry` dengan material fisik jernih (`MeshPhysicalMaterial`).
   - Sistem pergeseran verteks dinamis (vertex wave morphing) yang berdenyut mengikuti tingkat distorsi yang dihasilkan kecerdasan buatan.
   - Dua cincin orbit spasial (`THREE.TorusGeometry`) dengan rotasi independen dan partikel cahaya melayang.
   - Transisi warna halus (linear interpolation / lerp) dan rotasi reaktif terhadap respon suasana hati (mood) AI.

2. **Top Floating Pill Bar:**
   - Badge status mood AI real-time.
   - Selektor 4 Persona: Minimalis Sopan, Teman Santai, Mentor Tegas, dan Visioner Liar.
   - Pengatur parameter sampling model: Slider Temperature (0.1 - 1.4) dan Slider Top-P (0.1 - 1.0).
   - Form input API Key Gemini terlindungi (tipe password) dengan tombol pengalih visibilitas, otomatis tersimpan di `localStorage` peramban.

3. **Left Widget: Pomodoro Timer Interaktif:**
   - Penghitung waktu mundur 25:00 menit dengan tipografi angka tabular (`font-variant-numeric: tabular-nums`).
   - Tombol kontrol manual: Start, Pause, Reset, dan tombol preset durasi (25m, 15m, 5m).
   - Sinkronisasi otomatis: jika AI mengembalikan nilai `setTimerMinutes` lebih besar dari 0, timer akan langsung disetel dan berjalan secara otomatis.

4. **Right Widget: Smart To-Do List:**
   - Daftar checklist tugas dengan fitur penandaan selesai (coret teks), input manual tugas baru, dan tombol penghapusan.
   - Indikator counter produktivitas tugas (misal: "1/3 Selesai").
   - Penambahan otomatis: jika AI mengembalikan nilai `newTodo` non-kosong, item tugas baru otomatis disisipkan ke daftar tugas dengan lencana visual khusus.

5. **Bottom Clean Chat Dock:**
   - Gelembung obrolan kaca dua arah (User vs Jarvis).
   - Kolom masukan teks fleksibel dengan dukungan tombol Enter atau klik tombol Kirim.
   - Indikator visual loading atau proses berpikir saat AI memproses permintaan.
   - Tombol pintasan pertanyaan cepat (Quick Prompt Chips) untuk efisiensi interaksi.

6. **Dual-Mode AI Engine & Intelligent Local Fallback:**
   - Komunikasi REST API langsung ke endpoint Google Gemini `gemini-2.5-flash` dengan pengalihan otomatis ke `gemini-1.5-flash`.
   - Mengirimkan instruksi sistem persona (`systemInstruction`), riwayat obrolan multiturn (`contents`), dan memaksa balasan dalam format JSON terstruktur (`application/json`).
   - Mesin fallback lokal cerdas: jika panggilan jaringan terputus, API key belum valid, atau kuota habis, sistem tetap merespons dengan cerdas, menggerakkan bola 3D, memicu timer, dan menambahkan to-do tanpa menampilkan pesan error atau layar kosong.

---

## Arsitektur Berkas

```
/opt/data/jarvis-core/
├── RANCANGAN_PROYEK.md  # Dokumen arsitektur dan spesifikasi teknis mendalam
├── README.md            # Dokumentasi panduan penggunaan dan ikhtisar sistem
├── index.html           # Aplikasi web single-file Three.js lengkap
└── test_jarvis.py       # Test suite otomatis verifikasi fungsional & kualitas
```

---

## Konfigurasi Persona

| Persona | Karakter & Gaya Bahasa | Temp | Top-P | Warna Hex Default | Efek Visual 3D |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Minimalis Sopan** | Formal, sopan, ringkas, maksimal 3 kalimat | 0.30 | 0.40 | `#0284C7` (Sky Blue) | Rotasi lambat, distorsi gelombang minim |
| **Teman Santai** | Hangat, bersahabat, kasual, suportif | 0.75 | 0.80 | `#059669` (Emerald) | Rotasi sedang, denyut ramah |
| **Mentor Tegas** | Disiplin, berorientasi hasil, anti-distraksi | 0.20 | 0.30 | `#D97706` (Amber Focus) | Rotasi cepat, gerakan tajam terfokus |
| **Visioner Liar** | Imajinatif, kreatif, berpikir lateral | 1.15 | 0.95 | `#9333EA` (Electric Purple) | Rotasi dinamis, distorsi gelombang tinggi |

---

## Skema JSON Output

AI dikonfigurasi untuk selalu mengembalikan data dengan skema JSON terstruktur berikut:

```json
{
  "reply": "Pesan balasan teks Jarvis kepada pengguna",
  "moodLabel": "Label suasana hati (contoh: Fokus, Tenang, Kreatif)",
  "colorHex": "#0284C7",
  "rotationSpeed": 0.015,
  "distortion": 0.10,
  "newTodo": "Judul tugas baru (kosongkan jika tidak ada)",
  "setTimerMinutes": 0
}
```

---

## Petunjuk Penggunaan Cepat

### 1. Menjalankan Server Web Lokal
Karena aplikasi memuat Three.js melalui CDN dan beroperasi langsung di peramban, Anda dapat menjalankan server HTTP bawaan Python:

```bash
cd /opt/data/jarvis-core
python3 -m http.server 8080
```

Buka peramban di `http://localhost:8080`.

### 2. Konfigurasi API Key Gemini
- Aplikasi sudah terisi secara default dengan API Key pengguna pada kolom sandi di Floating Pill Bar atas.
- Kunci ini otomatis disimpan ke dalam `localStorage` peramban.
- Anda dapat mengubah kunci kapan saja melalui input tersebut atau menekan ikon mata untuk melihat karakter kunci.

### 3. Menguji Otomasi Perintah AI
Coba ketikkan perintah berikut ke dalam Chat Dock:
- *"Saya mau fokus coding selama 25 menit"* -> Pomodoro Timer di kiri akan otomatis berjalan pada 25:00.
- *"Tolong catat tugas: Selesaikan dokumentasi API"* -> Item baru akan otomatis muncul di kartu To-Do kanan.
- *"Ganti suasana ke mode kreatif penuh"* -> Bola 3D akan berubah warna menjadi ungu elektrik dengan distorsi gelombang dinamis.

---

## Pengujian Otomatis (Test Suite)

Proyek ini dilengkapi dengan suite pengujian otomatis Python untuk memvalidasi:
- Integritas berkas dan keberadaan elemen vital DOM di `index.html`.
- Kepatuhan absolut Zero Em-Dash (bebas karakter em dash dan en dash).
- Validasi skema parsing respons JSON.
- Ketahanan logika Pomodoro timer dan To-Do list.

Jalankan pengujian dengan perintah:
```bash
/opt/data/.venv/bin/python3 /opt/data/jarvis-core/test_jarvis.py
```

Seluruh pengujian dirancang untuk menghasilkan status 100% lolos (PASS).

---
*Catatan Kualitas: Dokumen dan kode ini sepenuhnya bebas dari karakter em dash dan en dash.*
