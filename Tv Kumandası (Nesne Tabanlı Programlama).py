#Bu kod nesne tabanlı programlama örneğidir.
import random
import msvcrt

class Kumanda ():
     def __init__(self, tv_durum="Kapalı", tv_ses=0,kanal_listesi= ["Trt"], kanal="Trt"):
          print("Kumanda oluşturuldu.")
          self.tv_ses = tv_ses
          self.tv_durum = tv_durum
          self.kanal_listesi = kanal_listesi
          self.kanal = kanal
          self.tv_acik_mi = False
     
     def sesi_azalt_artir(self):
          while True:
               karakter= input("Ses seviyesini azaltmak için '<', arttırmak için '>' tuşuna basın. Çıkmak için 'q' tuşuna basın: ")
               if karakter == "<":
                    self.tv_ses -= 1
                    print("Ses seviyesi:", self.tv_ses)
               elif karakter == ">":
                    self.tv_ses += 1
                    print("Ses seviyesi:", self.tv_ses)
               elif karakter == "q":
                    break
               else:
                    print("Geçersiz tuşlama. Lütfen tekrar deneyin.")

     def tv_kapat(self):
          if self.tv_durum == "Açık":
               print("TV kapatılıyor...")
               self.tv_durum = "Kapalı"
               self.tv_acik_mi = False
          else:
               print("TV zaten kapalı.")

     def tv_ac(self):
          if self.tv_durum == "Kapalı":
               print("TV açılıyor...")
               self.tv_durum = "Açık"
               self.tv_acik_mi = True
          else:
               print("TV zaten açık.")
     def __str__(self):
          return f"TV Durumu: {self.tv_durum}, Ses Seviyesi: {self.tv_ses}, Kanal: {self.kanal}"
     
     def __len__(self):
          return len(self.kanal_listesi)
     
     def rastgele_kanal(self):
          rastgele=random.randint(0,len(self.kanal_listesi)-1)
          self.kanal=self.kanal_listesi[rastgele]
          self.kanal=self.kanal_listesi[rastgele]

     def kanal_ekle(self, kanal_ismi):
          self.kanal_listesi.append(kanal_ismi)
          print(f"{kanal_ismi} kanalı eklendi.")  

kumanda=Kumanda()
print("""*********************************
      Televizyon Kumandası
      *********************************
      İşlemler:
      1. TV Aç
      2. TV Kapat
      3. Televizyon Bilgileri
      4. Kanal Sayısı Öğrenme
      5. Kanal Ekle
      6. Rastgele Kanal Aç
      7. Ses Seviyesini Azalt/Arttır
      **********************************""")
while True:
     işlem= input("Yapmak istediğiniz işlemi seçin (1-7): ")
     if işlem == "q":
          print("Programdan çıkılıyor...")
          break
     if işlem == "1":
          kumanda.tv_ac()
     elif işlem == "2":
          kumanda.tv_kapat()
     elif işlem == "3":
          print(kumanda)
     elif işlem == "4":
          print("Kanal sayısı:", len(kumanda))
     elif işlem == "5":
          kanal_ismi = input("Eklemek istediğiniz kanal ismini girin: ")
          kumanda.kanal_ekle(kanal_ismi)
     elif işlem == "6":
          kumanda.rastgele_kanal()
          print("Rastgele açılan kanal:", kumanda.kanal)
     elif işlem == "7":
          kumanda.sesi_azalt_artir()
     else:
          print("Geçersiz işlem. Lütfen tekrar deneyin.")
