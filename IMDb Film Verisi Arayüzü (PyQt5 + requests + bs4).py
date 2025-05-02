# Bu kod, PyQt5 ve BeautifulSoup kullanarak IMDb'de film arama yapar.
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys
import requests
from bs4 import BeautifulSoup

class IMDbFilm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IMDb Film Arama")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()
        self.film_adi = QLineEdit()
        self.film_adi.setPlaceholderText("Film adı girin")
        self.ara_buton = QPushButton("Ara")
        self.ara_buton.clicked.connect(self.film_ara)
        self.sonuc = QLabel("")

        layout.addWidget(self.film_adi)
        layout.addWidget(self.ara_buton)
        layout.addWidget(self.sonuc)

        self.setLayout(layout)

    def film_ara(self):
        film = self.film_adi.text().replace(" ", "+")
        url = f"https://www.imdb.com/find?q={film}"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            ilk_sonuc = soup.select_one(".findResult .result_text a")
            if ilk_sonuc:
                baslik = ilk_sonuc.text
                link = "https://www.imdb.com" + ilk_sonuc["href"]
                self.sonuc.setText(f"Bulundu: {baslik}\n{link}")
            else:
                self.sonuc.setText("Film bulunamadı.")
        except Exception as e:
            self.sonuc.setText(f"Hata: {str(e)}")

app = QApplication(sys.argv)
pencere = IMDbFilm()
pencere.show()
sys.exit(app.exec_())
