# RANCANGAN PROYEK: JARVIS CORE - 3D EMBODIED AI PRODUCTIVITY ASSISTANT

Dokumen arsitektur dan spesifikasi teknis lengkap untuk pembangunan antarmuka asisten produktivitas embodied 3D berbasis kecerdasan buatan Gemini API dan Three.js.

---

## 1. Project Overview

JARVIS CORE adalah antarmuka asisten produktivitas personal generasi baru yang menggabungkan kecerdasan buatan generatif multimodal (Google Gemini 2.5 Flash / 1.5 Flash) dengan perwujudan fisik digital 3D (3D Embodied AI Core). Berbeda dari chatbot konvensional yang kaku dalam kotak percakapan teks, JARVIS CORE menempatkan visualisasi bola energi 3D reaktif di panggung utama (Center-Stage), yang mengekspresikan kondisi emosional, tempo berpikir, dan persona asisten secara langsung melalui warna, kecepatan rotasi, serta gelombang distorsi geometris.

Sistem ini didesain dengan filosofi zero-build (berjalan instan tanpa bundler atau dependensi node_modules yang rumit), bertema Glassmorphism Light Mode kontemporer yang bersih, cerah, dan ergonomis, serta terintegrasi langsung dengan dua widget produktivitas utama: Pomodoro Timer dan Interactive To-Do List.

### Nilai Tambah Utama
1. **Embodied Presence:** Inti kecerdasan buatan memiliki representasi visual spasial nyata yang bereaksi dinamis terhadap percakapan.
2. **Action-Oriented AI:** Respon AI bukan sekadar teks, melainkan instruksi terstruktur (JSON) yang dapat memanipulasi widget sistem seperti memulai timer atau mencatat tugas to-do secara otomatis.
3. **Multi-Persona Adaptability:** Fleksibilitas gaya komunikasi melalui 4 persona terkalibrasi dengan parameter sampling kustom.
4. **Resilient Local Fallback:** Kemampuan beroperasi tanpa hambatan meskipun koneksi internet terputus atau kuota API tercapai berkat mesin simulasi lokal cerdas.

---

## 2. Requirements Mapping

Tabel berikut memetakan kebutuhan fungsional dan teknis proyek dengan implementasinya:

| Kebutuhan Fungsional | Komponen Solusi | Detail Implementasi Teknis |
| :--- | :--- | :--- |
| Visual 3D Inti Reaktif | Three.js WebGL Canvas | IcosahedronGeometry (subdivisi 4) dengan MeshPhysicalMaterial, cincin orbit ganda, partikel ambien, serta kalkulasi pergeseran verteks dinamis berbasis gelombang sinus-kosinus. |
| Glassmorphism Light Mode | CSS UI Overlay | Latar belakang Porcelain Slate (#F8FAFC), kontainer berkaca (white rgba 75%, backdrop-filter blur 16px, border lembut rgba 255 255 255 0.8, bayangan halus). |
| Navigasi Kontrol Atas | Top Floating Pill Bar | Dropdown 4 Persona, slider Temperature (0.1 - 1.4), slider Top-P (0.1 - 1.0), badge status mood real-time, dan input API key Gemini tersimpan di localStorage. |
| Pengingat Waktu Fokus | Left Widget Pomodoro | Penghitung mundur 25:00 menit tabular, tombol Start/Pause, Reset, preset cepat, dan pendengar otomatis jika AI memicu setTimerMinutes > 0. |
| Manajemen Tugas | Right Widget To-Do | Checklist tugas, status selesai bertanda coret, input manual tambah tugas, tombol hapus, dan penambahan otomatis jika AI memicu newTodo. |
| Percakapan Multiturn | Bottom Clean Chat Dock | Gelembung riwayat pesan bergaya kaca, input teks, tombol kirim, indikator berpikir, dan tombol pintasan prompt cerdas. |
| Komunikasi AI Eksternal | Google Gemini REST API | Endpoint gemini-2.5-flash dengan fallback otomatis ke gemini-1.5-flash, pengiriman systemInstruction, history contents, serta format keluaran application/json. |
| Ketahanan Sistem | Intelligent Local Fallback | Mesin inferensi lokal berbasis aturan jika fetch API gagal, menghasilkan respons kontekstual persona, aksi widget, dan perubahan visual 3D 100% mulus. |
| Kepatuhan Kualitas | Anti-Slop & Zero Em Dash | Eliminasi mutlak karakter em dash dan en dash, tipografi tabular numbers, tombol bertransisi taktil active:scale-95. |

---

## 3. Desain Interface Center-Stage

### 3.1 Hierarki Visual dan Penataan Ruang
Antarmuka JARVIS CORE disusun dengan teknik layered viewport:
1. **Lapisan 0 (Background Canvas):** Three.js WebGL Renderer memenuhi 100vw x 100vh di latar belakang. Bola 3D terletak tepat di tengah layar dengan kamera berorientasi perspektif (FOV 45 derajat).
2. **Lapisan 1 (Top Navigation):** Floating Pill Bar melayang di bagian atas layar (top: 24px), diposisikan di tengah menggunakan transform translateX(-50%).
3. **Lapisan 2 (Samping Kiri & Kanan):**
   - Left Widget (Pomodoro Timer) melayang di sisi kiri (left: 28px, top: 120px, lebar 280px).
   - Right Widget (To-Do List) melayang di sisi kanan (right: 28px, top: 120px, lebar 320px).
4. **Lapisan 3 (Bottom Dock):** Chat Dock melayang di bagian bawah layar (bottom: 24px, lebar maksimum 840px, lebar relatif 92vw).

### 3.2 Spesifikasi Glassmorphism Light Mode
- **Kanvas Latar Belakang:** Porcelain Slate `#F8FAFC` dengan gradasi radial lembut `#FFFFFF` di tengah dan aksen subtle `#E2E8F0` di sudut-sudut.
- **Permukaan Kaca (Glass Containers):**
  - Background: `rgba(255, 255, 255, 0.72)` hingga `rgba(255, 255, 255, 0.85)`
  - Backdrop Filter: `blur(16px) saturate(180%)`
  - Border: `1px solid rgba(255, 255, 255, 0.75)` dengan inset shadow halus
  - Box Shadow: `0 12px 32px -4px rgba(15, 23, 42, 0.08), 0 4px 12px -2px rgba(15, 23, 42, 0.04)`
  - Radius Sudut: `20px` untuk widget kartu samping, `9999px` untuk floating pill bar atas, `24px` untuk chat dock bawah.
- **Tipografi:** Keluarga font sans-serif proporsional bersih (`system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`). Angka timer dan persentase menggunakan `font-variant-numeric: tabular-nums` agar tidak bergetar saat digit berganti.

### 3.3 Visual 3D Core Three.js
- **Geometri Inti:** `THREE.IcosahedronGeometry(2.0, 4)` yang menghasilkan sekitar 1.280 permukaan segitiga halus.
- **Material Inti:** `THREE.MeshPhysicalMaterial` dengan properti:
  - `metalness`: 0.15
  - `roughness`: 0.2
  - `clearcoat`: 0.8
  - `clearcoatRoughness`: 0.15
  - `transmission`: 0.1
  - `reflectivity`: 0.9
- **Vertex Wave Morphing Dinamis:**
  Posisi asli verteks disimpan dalam buffer array terpisah. Pada setiap frame animasi, posisi setiap verteks dihitung ulang berdasarkan waktu, frekuensi spasial, dan parameter distorsi:
  ```javascript
  const wave = Math.sin(origX * 2.5 + time * 3.0) * Math.cos(origY * 2.5 + time * 2.0) * currentDistortion * 0.45;
  const factor = 1.0 + wave / radius;
  posAttr.setXYZ(i, origX * factor, origY * factor, origZ * factor);
  ```
- **Cincin Orbit Spasial:** Dua cincin torus tipis (`THREE.TorusGeometry(3.0, 0.02, 16, 120)` dan `THREE.TorusGeometry(3.6, 0.015, 16, 120)`) berputar pada sumbu X dan Z yang condong untuk memberikan kedalaman kosmik modern.
- **Pencahayaan Tri-Point:**
  - Ambient Light: `THREE.AmbientLight(0xffffff, 0.85)`
  - Key Directional Light: `THREE.DirectionalLight(0xffffff, 1.2)` dari posisi (5, 8, 6)
  - Reaktif Point Light: `THREE.PointLight(colorHex, 2.0, 15)` di posisi (0, 0, 3) yang warnanya bertransisi halus mengikuti suasana hati AI.

---

## 4. Diagram Pipeline

Berikut adalah arsitektur alur data dari masukan pengguna hingga pembaruan antarmuka dan visual 3D:

```
[ PENGGUNA ]
     |
     v
[ Input Chat Dock ] ---> (Event: Form Submit / Quick Prompt)
     |
     v
[ State Manager (App State) ]
     |--- Ambil Persona Aktif (System Instruction)
     |--- Ambil Parameter Sampling (Temperature & Top-P)
     |--- Ambil Riwayat Percakapan (Multi-Turn Contents)
     |--- Ambil Gemini API Key dari localStorage / UI
     |
     +-------------------------------------------------+
     |                                                 |
     v                                                 v
[ Jalur Utama: REST API ]                  [ Kondisi Gangguan / Gagal ]
  URL: gemini-2.5-flash / gemini-1.5-flash             |
  Payload: JSON { systemInstruction, contents, ... }   |
     |                                                 |
     | (Success: HTTP 200)                             v
     |                                      [ Intelligent Local Fallback Engine ]
     |                                      - Evaluasi intent masukan via regex/aturan
     |                                      - Tentukan status persona & respon cerdas
     |                                      - Ekstraksi waktu timer & tugas todo
     |                                                 |
     +------------------------+------------------------+
                              |
                              v
                   [ JSON Response Parser ]
                   - Parse structured output:
                     * reply (string)
                     * moodLabel (string)
                     * colorHex (string #RRGGBB)
                     * rotationSpeed (number)
                     * distortion (number)
                     * newTodo (string)
                     * setTimerMinutes (number)
                              |
         +--------------------+--------------------+
         |                    |                    |
         v                    v                    v
  [ Visual 3D Engine ]  [ Pomodoro Widget ]  [ To-Do Widget ]
  - Lerp Mesh Color     - Jika minutes > 0:  - Jika newTodo != "":
  - Lerp PointLight       Set durasi baru      Tambah item tugas
  - Update Rotation Spd   Auto-start timer     Beri highlight badge
  - Update Wave Morph   - Update tampilan      Update status counter
         |
         v
  [ Chat History Bubble ]
  - Render jawaban teks Jarvis
  - Tampilkan mood badge dan timestamp
  - Hapus indikator loading
```

---

## 5. Konfigurasi Parameter 4 Persona

JARVIS CORE dilengkapi dengan 4 persona yang masing-masing memiliki profil kognitif, konfigurasi sampling, dan ekspresi visual yang unik:

### 5.1 Persona 1: Minimalis Sopan
- **Karakter:** Ringkas, sangat sopan, langsung pada pokok masalah tanpa berbasa-basi panjang, menenangkan.
- **Target Penggunaan:** Pekerjaan administratif cepat, pertanyaan factual kilat, sesi fokus tinggi.
- **Parameter Sampling:**
  - Temperature: `0.30`
  - Top-P: `0.40`
- **Konfigurasi Visual Default:**
  - Mood Label: `Tenang & Terfokus`
  - Color Hex: `#0284C7` (Sky Blue sejuk)
  - Rotation Speed: `0.008` (putaran lambat menenangkan)
  - Distortion: `0.05` (denyut gelombang sangat halus)
- **Instruksi Khusus:** Gunakan bahasa Indonesia yang santun, formal, efisien, dan tidak lebih dari 3 kalimat kecuali diminta rincian teknis.

### 5.2 Persona 2: Teman Santai
- **Karakter:** Hangat, ramah, bersahabat, menggunakan gaya bahasa percakapan sehari-hari yang suportif, optimis.
- **Target Penggunaan:** Sesi kerja harian, brainstorming santai, teman berbincang pengusir lelah.
- **Parameter Sampling:**
  - Temperature: `0.75`
  - Top-P: `0.80`
- **Konfigurasi Visual Default:**
  - Mood Label: `Santai & Hangat`
  - Color Hex: `#059669` (Emerald Green segar)
  - Rotation Speed: `0.015` (ritme moderat stabil)
  - Distortion: `0.15` (gelombang bervolume ramah)
- **Instruksi Khusus:** Gunakan gaya percakapan yang santai namun tetap jelas dan membantu, boleh menggunakan kata sapaan akrab seperti "Halo kawan" atau "Siap, santai saja".

### 5.3 Persona 3: Mentor Tegas
- **Karakter:** Disiplin, berorientasi hasil, tegas, menuntut fokus tinggi, menolak penundaan (anti-prokrastinasi).
- **Target Penggunaan:** Sesi kerja maraton, target deadline ketat, eksekusi tugas berat.
- **Parameter Sampling:**
  - Temperature: `0.20`
  - Top-P: `0.30`
- **Konfigurasi Visual Default:**
  - Mood Label: `Fokus Eksekusi`
  - Color Hex: `#D97706` (Amber / Crimson Focus)
  - Rotation Speed: `0.028` (rotasi tegas cepat)
  - Distortion: `0.10` (gerakan kaku dan berorientasi presisi)
- **Instruksi Khusus:** Tekankan pentingnya efisiensi waktu, ingatkan target deadline, instruksikan pengguna untuk langsung mengeksekusi tindakan nyata, jangan mentolerir alasan penundaan.

### 5.4 Persona 4: Visioner Liar
- **Karakter:** Kreatif tanpa batas, penuh imajinasi, berpikir lateral, provokatif secara intelektual, metaforis.
- **Target Penggunaan:** Ideation produk baru, penulisan kreatif, eksplorasi konsep futuristik.
- **Parameter Sampling:**
  - Temperature: `1.15`
  - Top-P: `0.95`
- **Konfigurasi Visual Default:**
  - Mood Label: `Eksplorasi Kreatif`
  - Color Hex: `#9333EA` (Electric Violet / Purple)
  - Rotation Speed: `0.040` (rotasi dinamis cepat)
  - Distortion: `0.45` (gelombang distorsi verteks dramatis)
- **Instruksi Khusus:** Hubungkan konsep-konsep yang tidak biasa, berikan sudut pandang radikal dan solutif, gunakan analogi masa depan dan dorong batas eksperimentasi.

---

## 6. Skema JSON Output (responseSchema)

Seluruh tanggapan dari kecerdasan buatan diwajibkan mengikuti skema JSON baku berikut:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "JarvisCoreResponse",
  "type": "object",
  "properties": {
    "reply": {
      "type": "string",
      "description": "Teks jawaban atau dialog Jarvis kepada pengguna sesuai persona aktif."
    },
    "moodLabel": {
      "type": "string",
      "description": "Label singkat status emosi atau mode visual AI saat ini, contoh: Fokus Tajam, Tenang, Kreatif Liar."
    },
    "colorHex": {
      "type": "string",
      "pattern": "^#[0-9A-Fa-f]{6}$",
      "description": "Kode warna heksadesimal 6 karakter untuk mengubah warna bola Three.js dan lampu pointLight."
    },
    "rotationSpeed": {
      "type": "number",
      "minimum": 0.002,
      "maximum": 0.1,
      "description": "Kecepatan perputaran bola 3D per frame."
    },
    "distortion": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 0.6,
      "description": "Tingkat distorsi gelombang verteks pada permukaan bola 3D."
    },
    "newTodo": {
      "type": "string",
      "description": "Judul tugas baru untuk ditambahkan ke widget To-Do List. String kosong jika tidak ada tugas yang perlu dicatat."
    },
    "setTimerMinutes": {
      "type": "integer",
      "minimum": 0,
      "maximum": 180,
      "description": "Durasi menit untuk Pomodoro Timer jika pengguna meminta timer fokus atau istirahat. Bernilai 0 jika tidak mengubah timer."
    }
  },
  "required": [
    "reply",
    "moodLabel",
    "colorHex",
    "rotationSpeed",
    "distortion",
    "newTodo",
    "setTimerMinutes"
  ],
  "additionalProperties": false
}
```

### Contoh Payload Respon Valid
```json
{
  "reply": "Timer fokus 25 menit telah diaktifkan. Singkirkan semua distraksi dan selesaikan modul autentikasi sekarang.",
  "moodLabel": "Disiplin Penuh",
  "colorHex": "#D97706",
  "rotationSpeed": 0.030,
  "distortion": 0.12,
  "newTodo": "Selesaikan unit test auth controller",
  "setTimerMinutes": 25
}
```

---

## 7. Skenario Demo Pengujian

Untuk memastikan seluruh integrasi bekerja 100%, berikut adalah 7 skenario pengujian fungsional:

1. **Skenario Percakapan Dasar & Reaksi 3D:**
   - Masukan: "Halo Jarvis, apa kabarmu hari ini?"
   - Ekspektasi: Teks jawaban muncul di bubble chat dock, bola 3D berdenyut dan berubah warna secara halus mengikuti persona aktif.
2. **Skenario Perubahan Persona:**
   - Tindakan: Mengubah dropdown dari "Minimalis Sopan" ke "Visioner Liar".
   - Ekspektasi: Slider temperature otomatis naik ke 1.15, top-P ke 0.95, warna inti bertransisi ke ungu (#9333EA), rotasi meningkat, dan distorsi gelombang menjadi aktif.
3. **Skenario Perintah Pomodoro Otomatis:**
   - Masukan: "Saya butuh waktu fokus 25 menit untuk coding."
   - Ekspektasi: JSON respon menyertakan `setTimerMinutes: 25`, widget timer Pomodoro di sebelah kiri langsung ter-reset ke 25:00 dan otomatis berjalan (countdown aktif).
4. **Skenario Perintah Tambah Tugas To-Do:**
   - Masukan: "Ingatkan saya untuk push kode ke GitHub sebelum makan siang."
   - Ekspektasi: JSON respon menyertakan `newTodo: "Push kode ke GitHub sebelum makan siang"`, item baru seketika muncul di kartu To-Do List kanan dengan badge animasi hijau.
5. **Skenario Eksekusi Aksi Ganda (Timer + To-Do):**
   - Masukan: "Mulai sesi sprint 15 menit dan catat tugas: Tinjau PR antarmuka."
   - Ekspektasi: Timer kiri berganti ke 15:00 dan mulai berhitung, checklist kanan bertambah tugas baru, bola 3D beralih ke mode fokus.
6. **Skenario Interaktivitas Manual Widget:**
   - Tindakan: Klik checklist tugas untuk menandai selesai, klik tombol hapus, klik tombol Start/Pause dan Reset pada Pomodoro, atur slider temperature secara manual.
   - Ekspektasi: Seluruh kontrol UI merespons seketika tanpa ada kontrol mati (no dead controls).
7. **Skenario Ketahanan Offline / Local Fallback:**
   - Tindakan: Mengisi API key sembarang atau memutuskan koneksi internet, lalu mengirim pesan "Bantu saya rancang ide proyek baru".
   - Ekspektasi: Mesin fallback lokal langsung mengambil alih dalam waktu kurang dari 100 milidetik, menghasilkan tanggapan cerdas lengkap dengan parameter 3D dan aksi widget tanpa pesan error mengganggu.

---

## 8. Panduan Setup dan Menjalankan

### Persyaratan Sistem
- Web browser modern dengan dukungan WebGL dan Web Audio (Chrome, Firefox, Edge, Safari).
- Python 3.10+ untuk menjalankan server lokal dan test suite otomatis.

### Langkah Menjalankan
1. Masuk ke direktori proyek:
   ```bash
   cd /opt/data/jarvis-core
   ```
2. Jalankan pengujian verifikasi otomatis:
   ```bash
   /opt/data/.venv/bin/python3 test_jarvis.py
   ```
3. Jalankan HTTP server lokal:
   ```bash
   python3 -m http.server 8080
   ```
4. Buka peramban pada alamat `http://localhost:8080`.

---
*Dokumen ini disusun tanpa karakter em dash maupun en dash sesuai standar kualitas anti-slop.*
