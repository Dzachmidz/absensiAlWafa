<div align="center">

# 📋 Sistem Informasi Absensi Al Wafa

### _A production-grade, IoT-integrated automated attendance management system built with Django._

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-Latest-red?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)]()

</div>

---

## 📌 Overview

**Sistem Informasi Absensi Al Wafa** adalah sistem manajemen absensi berbasis RFID yang dirancang untuk lingkungan pendidikan nyata. Sistem ini menggantikan proses pencatatan kehadiran manual dengan solusi digital otomatis menggunakan kartu RFID yang terintegrasi langsung dengan hardware scanner (IoT device).

Sistem ini dibangun dengan arsitektur **monolitik modular** menggunakan Django, mengekspos **REST API** untuk komunikasi dengan perangkat keras RFID, dan menyediakan **panel admin berbasis web** yang kaya fitur untuk pengelolaan data siswa, kelas, jadwal, dan laporan kehadiran.

> Sistem ini telah digunakan secara aktif di lingkungan institusi pendidikan **Al Wafa**, mengelola data kehadiran siswa secara real-time setiap hari.

---

## ✨ Features

- 🔐 **Autentikasi Admin** — Login/logout aman berbasis session Django, seluruh halaman admin dilindungi `@login_required`
- 📡 **Integrasi Hardware RFID** — REST API endpoint khusus untuk menerima scan UID dari perangkat RFID (ESP32/Arduino)
- ⏱️ **Deteksi Status Otomatis** — Sistem secara cerdas menentukan status kehadiran: **Hadir**, **Terlambat**, atau **Telat Jemput** berdasarkan jam scan
- 🔄 **Multi-Sesi per Kelas** — Setiap kelas dapat memiliki beberapa sesi jadwal (Pagi/Sore), dengan toleransi waktu masuk/pulang yang dapat dikonfigurasi
- 📊 **Dashboard Real-Time** — Menampilkan total siswa, jumlah hadir hari ini, jumlah belum hadir, dan aktivitas absensi terbaru
- 👤 **Manajemen Siswa Lengkap** — CRUD siswa, import massal via file Excel, dan edit data individual
- 🏫 **Manajemen Kelas & Jadwal** — Kelola kelas beserta jadwal masuk & pulang per kelas, termasuk sesi jadwal khusus
- 🪪 **Registrasi Kartu RFID** — Daftarkan UID kartu RFID ke data siswa, dengan fitur pengecekan status kartu (sudah terdaftar / tersedia)
- ✍️ **Absensi Manual** — Entri absensi diluar RFID oleh admin untuk kondisi darurat
- 📜 **Riwayat Absensi** — Tabel histori lengkap seluruh data kehadiran dengan filter dan pagination
- 📤 **Export ke Excel** — Unduh laporan absensi dalam format `.xlsx` menggunakan `openpyxl`
- ⚙️ **Pengaturan Waktu Global** — Konfigurasi jam operasional global sistem dengan pola Singleton

---

## 🏗️ Architecture

Sistem ini menggunakan arsitektur **Django MTV (Model-Template-View)** dengan dua modul aplikasi utama yang terpisah secara bertanggung jawab:

```
┌────────────────────────────────────────────┐
│         Browser / Admin Client             │
└──────────────────┬─────────────────────────┘
                   │ HTTP Request
┌──────────────────▼─────────────────────────┐
│            Django URL Router               │
│    (absensi/urls.py → app-level urls)      │
└──────────┬───────────────────┬─────────────┘
           │                   │
┌──────────▼──────────┐  ┌─────▼─────────────┐
│  adminapp (Web UI)  │  │  userapp (REST API)│
│  - Dashboard        │  │  - /api/rfid-scan/ │
│  - Data Siswa/Kelas │  │  - Serializers     │
│  - Riwayat Absensi  │  │  - Absensi Logic   │
│  - RFID Registrasi  │  └─────┬─────────────┘
│  - Absensi Manual   │        │ POST UID
└──────────┬──────────┘  ┌─────▼────────────┐
           │              │  RFID Hardware   │
┌──────────▼──────────────┤  (ESP32/Arduino) │
│      Data Models        └──────────────────┘
│  Siswa | Kelas | Absensi                   │
│  JadwalSesi | RfidLog                      │
│  WaktuOperasional (Singleton)              │
└──────────┬─────────────────────────────────┘
           │ SQL / ORM
┌──────────▼─────────────────────────────────┐
│         Database (SQLite / MySQL)           │
└────────────────────────────────────────────┘
```

### Modul Utama:

- **`userapp`** — Mengelola model data inti (`Siswa`, `Kelas`, `Absensi`, `JadwalSesi`, `RfidLog`, `WaktuOperasional`), REST API untuk hardware RFID, dan logika absensi otomatis.
- **`adminapp`** — Mengelola seluruh tampilan web admin: dashboard, manajemen data, registrasi RFID, riwayat absensi, dan fitur ekspor/impor data.

### Mekanisme Absensi Otomatis:

1. Hardware RFID mengirim `POST /api/rfid-scan/` dengan payload `{"uid": "XXXX"}`
2. Sistem mencari `Siswa` berdasarkan UID kartu
3. Jika ditemukan, sistem menentukan **mode absensi** (`masuk` / `pulang`) berdasarkan:
   - Ada/tidaknya record `Absensi` terbuka (jam_keluar null) hari ini
   - Jadwal waktu dari sesi kelas yang relevan
4. Status kehadiran dihitung otomatis: `Tepat Waktu` atau `Terlambat`
5. Response JSON dikirim kembali ke hardware (nama siswa, mode, pesan)

---

## 🔄 System Workflow

### Alur Absensi Masuk (Check-In)

```
[Tap Kartu RFID]
      │
      ▼
[Hardware POST → /api/rfid-scan/]
      │
      ▼
[Cari Siswa by RFID UID]
      │
      ├── Tidak Ditemukan → Log RfidLog (status: unknown) → Response Error
      │
      └── Ditemukan
              │
              ▼
      [Ambil Jadwal Kelas / Sesi Aktif]
              │
              ▼
      [Hitung Status: Tepat Waktu / Terlambat]
              │
              ▼
      [Simpan record Absensi ke Database]
              │
              ▼
      [Response: "Selamat Datang, {Nama}"]
```

### Alur Absensi Pulang (Check-Out)

```
[Tap Kartu RFID ke-2]
      │
      ▼
[Sistem deteksi ada open_absensi hari ini (jam_keluar = null)]
      │
      ▼
[Cek waktu saat ini >= jadwal_pulang_mulai]
      │
      ├── Belum Waktunya → Response: "Anda sudah absen masuk pukul HH:MM"
      │
      └── Sudah Waktunya
              │
              ▼
      [Update jam_keluar pada record Absensi]
              │
              ▼
      [Response: "Selamat Jalan, {Nama}"]
```

### Alur Admin Panel

```
1. Admin login → /login/ (session-based auth)
2. Dashboard → Lihat ringkasan hadir/tidak hadir hari ini
3. Kelola Kelas → Tambah/edit kelas + konfigurasi jadwal sesi
4. Kelola Siswa → CRUD + import Excel massal
5. Registrasi RFID → Daftarkan/cek kartu ke siswa
6. Absensi Manual → Input absensi tanpa RFID
7. Riwayat Absensi → Filter & export laporan ke Excel
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/absensiDigital.git
   cd absensiDigital
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser (Admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/login` to access the admin panel.

### RFID Hardware Integration

The system exposes a REST API endpoint for the RFID scanner device:

```
POST /api/rfid-scan/
Content-Type: application/json

{
  "uid": "A1B2C3D4"
}
```

Configure your ESP32/Arduino to send `POST` requests to this endpoint when a card is tapped.

---