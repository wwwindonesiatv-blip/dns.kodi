# 🌐 Google DNS Auto-Switch for Kodi (Android)

[![Kodi Repo Deploy](https://github.com/wwwindonesiatv-blip/dns.kodi/actions/workflows/deploy.yml/badge.svg)](https://github.com/wwwindonesiatv-blip/dns.kodi/actions)
[![Platform](https://img.shields.io/badge/Platform-Android-green.svg)](https://www.android.com/)

Repositori ini menyediakan update otomatis untuk addon **Google DNS Auto**. Addon ini dirancang khusus untuk pengguna Kodi di perangkat Android guna memastikan koneksi internet selalu menggunakan Google DNS (IPv4 & IPv6).

## 🚀 Fitur Utama
- **Otomatis:** Mengubah setting DNS sistem Android saat Kodi dijalankan.
- **Support Modern Android:** Menggunakan mode `Private DNS` (DNS-over-TLS) dengan hostname `dns.google`.
- **Tanpa Pengaturan:** Cukup install dan aktifkan, script akan bekerja di latar belakang.
- **Auto-Update:** Repositori ini akan memberikan update otomatis ke Kodi Anda jika ada versi baru.

## 🛠️ Cara Instalasi di Kodi
Untuk mendapatkan update otomatis, disarankan menginstal melalui alamat Repository:

1. Buka **Kodi** > **Settings** (ikon Gear).
2. Pilih **File Manager** > **Add Source**.
3. Klik **<None>** dan masukkan URL berikut:
   `https://wwwindonesiatv-blip.github.io/dns.kodi/zips/`
4. Beri nama sumber ini `.DNS` lalu klik OK.
5. Kembali ke menu utama Kodi, pilih **Add-ons**.
6. Klik ikon **Package Installer** (kotak terbuka) di pojok kiri atas.
7. Pilih **Install from zip file** > pilih `.DNS`.
8. Klik file `repository.dns.google-x.x.x.zip`.
9. Setelah terpasang, pilih **Install from repository** > **Google DNS Repository**.
10. Masuk ke **Services** > **Google DNS Auto** > **Install**.

## 📝 Catatan Penting
* **Hanya Android:** Script ini menggunakan perintah shell `settings put global` yang hanya ada di sistem operasi Android.
* **Izin Write Settings:** Pada beberapa versi Android, Kodi mungkin memerlukan izin untuk mengubah pengaturan sistem.
* **Private DNS:** Script ini mengatur Android ke mode "Private DNS Provider Hostname".

## 🏗️ Struktur Repositori
- `script.dns.google.auto/`: Kode sumber utama addon (Python).
- `docs/`: Folder otomatis untuk GitHub Pages (berisi file ZIP dan `addons.xml`).
- `deploy.yml`: Workflow otomatis yang menangani pembuatan paket ZIP dan update repository.

---
**Maintained by:** [dns kodi](https://github.com/wwwindonesiatv-blip)
