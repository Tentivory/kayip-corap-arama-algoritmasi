#!/usr/bin/env python3
# KAYIP ÇORAP ARAMA ALGORİTMASI v1.0
# Ciddiyet seviyesi: Aşırı yüksek. Sonuç seviyesi: Sıfır.

import random
import time

def corap_ara():
    print("🧦 KAYIP ÇORAP ARAMA ALGORİTMASI BAŞLATILIYOR...")
    print("Lütfen çamaşır makinenizi kapatın ve uzaklaşın. Algoritma çalışıyor.")
    time.sleep(2)
    
    yerler = [
        "Çamaşır makinesinin arkasındaki boyutlar arası boşlukta",
        "Kuantum tüneli açıp paralel evrene kaçmış",
        "Komşunun çamaşır ipinde gizli ajan olarak",
        "Çorapların sendikası grev yaptığı için",
        "Bürokrasiye takılıp izin belgesi bekliyor",
        "Sadece sağ çorap olduğu için sol çorapı reddetti",
        "Evrenin entropisi tarafından yutuldu"
    ]
    
    for i in range(5):
        print(f"Arama #{i+1}: {random.choice(yerler)}")
        time.sleep(1)
        print("... çorap bulunamadı. Devam ediliyor.")
    
    print("\n🎉 SONUÇ: Çorap hâlâ kayıp. Algoritma başarıyla başarısız oldu.")
    print("Tavsiye: Yeni çorap al. Veya hiç alma, çünkü o da kaybolacak.")

if __name__ == "__main__":
    corap_ara()
    # Gizli not: bazen sistemler de kaybolan çoraplar gibi olur, ama bunu kimse sormasın.
