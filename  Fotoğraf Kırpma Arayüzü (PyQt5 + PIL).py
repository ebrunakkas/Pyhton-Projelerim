#Bu kod, PyQt5 ve PIL (Pillow) kütüphanelerini kullanarak basit bir fotoğraf kırpma uygulaması oluşturur.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout
from PIL import Image
import sys

class FotografKirpici(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fotoğraf Kırpıcı")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label = QLabel("Bir fotoğraf seçin ve kırpın.")
        self.buton = QPushButton("Fotoğraf Seç")
        self.buton.clicked.connect(self.kirp)

        layout.addWidget(self.label)
        layout.addWidget(self.buton)
        self.setLayout(layout)

    def kirp(self):
        dosya, _ = QFileDialog.getOpenFileName(self, "Fotoğraf Seç", "", "Images (*.png *.jpg)")
        if dosya:
            img = Image.open(dosya)
            kirpilmis = img.crop((50, 50, img.width - 50, img.height - 50))
            kayit_yolu = dosya.replace(".", "_kirpildi.")
            kirpilmis.save(kayit_yolu)
            self.label.setText(f"Kırpıldı: {kayit_yolu}")

app = QApplication(sys.argv)
pencere = FotografKirpici()
pencere.show()
sys.exit(app.exec_())
