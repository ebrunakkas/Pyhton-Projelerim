# Bu kod, PyQt5 ve BeautifulSoup kullanarak döviz bilgilerini çeken basit bir GUI uygulamasıdır.    
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys
import requests
from bs4 import BeautifulSoup

class DovizUygulamasi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Döviz Uygulaması")
        self.setGeometry(100, 100, 300, 200)
        
        self.layout = QVBoxLayout()

        self.buton = QPushButton("Döviz Bilgilerini Getir")
        self.buton.clicked.connect(self.verileri_getir)
        
        self.sonuc = QLabel("Henüz veri yok.")
        
        self.layout.addWidget(self.buton)
        self.layout.addWidget(self.sonuc)

        self.setLayout(self.layout)

    def verileri_getir(self):
        url = "https://www.doviz.com/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        dolar = soup.select_one(".dovizBar .item:nth-child(1) .value").text.strip()
        euro = soup.select_one(".dovizBar .item:nth-child(2) .value").text.strip()
        altin = soup.select_one(".dovizBar .item:nth-child(3) .value").text.strip()
        self.sonuc.setText(f"Dolar: {dolar}\nEuro: {euro}\nAltın: {altin}")

app = QApplication(sys.argv)
pencere = DovizUygulamasi()
pencere.show()
sys.exit(app.exec_())
