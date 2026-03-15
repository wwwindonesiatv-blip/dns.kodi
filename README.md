# DNS Kodi Repository

Repository Kodi untuk Auto DNS Changer addon - Khusus Android devices.

![Kodi](https://img.shields.io/badge/Kodi-20%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Android-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📦 Addon yang Tersedia

### Google DNS Auto v1.0.0
- ✅ Otomatis ubah DNS ke Google DNS (8.8.8.8) setiap Kodi start
- ✅ Support IPv4 (8.8.8.8) + IPv6 (2001:4860:4860::8888)
- ✅ Khusus Android (Firestick, Android Box, Shield TV, MECOOL)
- ✅ Tanpa root, tanpa pengaturan manual
- ✅ Background service - jalan otomatis

## 🚀 Cara Install Repository

### Method 1: Download ZIP (Paling Mudah) ⭐

1. **Download file ini:**

2. **Install di Kodi:**
- Add-ons → Install from zip file
- Pilih file ZIP yang didownload
- Tunggu notifikasi "DNS Kodi Repository enabled"

### Method 2: File Manager (Recommended untuk Firestick)

1. **Di Kodi:** Settings → File Manager → Add source
2. **URL:** `https://github.com/USERNAME/dns.kodi/raw/main/`
3. **Name:** `DNS Kodi Repo`
4. **OK**
5. **Install:**
- Add-ons → Install from zip file
- Pilih "DNS Kodi Repo"
- `zips` → `repository.dns.kodi` → install ZIP

## 📥 Install Addon dari Repository

Setelah repository terinstall:

1. **Add-ons** → **Install from repository**
2. Pilih **"DNS Kodi Repository"**
3. **Services** → **Google DNS Auto**
4. Klik **Install**
5. **Restart Kodi** → DNS otomatis berubah!

## ⚙️ Cara Kerja

Setiap kali Kodi dibuka, DNS otomatis berubah ke:
- **IPv4:** 8.8.8.8 / 8.8.4.4
- **IPv6:** 2001:4860:4860::8888 / 2001:4860:4860::8844

## 🔧 Troubleshooting

### Q: Addon tidak jalan?
**A:** 
- Pastikan device **Android 9+** (Private DNS feature)
- Restart Kodi setelah install
- Cek System → Logging untuk error

### Q: Cara cek DNS sudah berubah?
**A:** 
Via ADB:
```bash
adb shell settings get global private_dns_specifier
# Output: dns.google

**B:** 
https://www.dnsleaktest.com
