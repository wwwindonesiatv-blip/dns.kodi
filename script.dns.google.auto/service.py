# type: ignore
import xbmc, os, time

def log(msg):
    xbmc.log("[Google DNS Auto] {}".format(msg), xbmc.LOGINFO)

class GoogleDNSAuto:
    def __init__(self):
        self.monitor = xbmc.Monitor()
        
    def apply_dns(self):
        # Tunggu 5 detik setelah Kodi start
        if self.monitor.waitForAbort(5):
            return
        
        try:
            # Ubah ke Google DNS (IPv4 + IPv6)
            os.system('settings put global private_dns_mode hostname')
            os.system('settings put global private_dns_specifier "dns.google"')
            
            log("DNS otomatis diubah ke Google DNS (8.8.8.8)")
            xbmc.executebuiltin('Notification(Google DNS Auto,DNS berhasil diubah ke Google DNS,5000,DefaultIconInfo.png)')
            
        except Exception as e:
            log("Error: {}".format(str(e)))
            xbmc.executebuiltin('Notification(Google DNS Auto,Gagal ubah DNS!,5000,DefaultIconError.png)')
    
    def run(self):
        self.apply_dns()

if __name__ == "__main__":
    log("Service dimulai - Auto Google DNS")
    service = GoogleDNSAuto()
    service.run()
    log("DNS berhasil diset ke Google")
