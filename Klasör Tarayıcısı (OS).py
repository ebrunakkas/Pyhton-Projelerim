#Bu script, geçerli dizindeki ve alt dizinlerdeki belirli uzantılara sahip dosyaları arar ve bulduğu dosyaların tam yollarını belirtilen bir dosyaya kaydeder.
import os

def dosyalari_ara_kaydet(uzanti, dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        for klasor_yolu, klasorler, dosyalar in os.walk("."): 
            for dosya in dosyalar:
                if dosya.endswith(uzanti):
                    tam_yol = os.path.join(klasor_yolu, dosya)
                    f.write(tam_yol + "\n")

dosyalari_ara_kaydet(".pdf", "pdf_dosyalari.txt")
dosyalari_ara_kaydet(".mp4", "mp4_dosyalari.txt")
dosyalari_ara_kaydet(".txt", "txt_dosyalari.txt")

print("Dosyalar bulundu ve kaydedildi.")
