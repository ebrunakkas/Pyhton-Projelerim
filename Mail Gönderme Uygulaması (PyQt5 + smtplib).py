# Bu kod, PyQt5 kullanarak bir mail gönderme uygulaması oluşturur.
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton
import smtplib
from email.message import EmailMessage
import sys

class MailGonder(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mail Gönderici")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.kime = QLineEdit()
        self.kime.setPlaceholderText("Alıcı Email")

        self.konu = QLineEdit()
        self.konu.setPlaceholderText("Konu")

        self.icerik = QTextEdit()
        self.icerik.setPlaceholderText("Mesajınız")

        self.gonder_buton = QPushButton("Gönder")
        self.gonder_buton.clicked.connect(self.mail_gonder)

        self.bilgi = QLabel("")

        layout.addWidget(self.kime)
        layout.addWidget(self.konu)
        layout.addWidget(self.icerik)
        layout.addWidget(self.gonder_buton)
        layout.addWidget(self.bilgi)

        self.setLayout(layout)

    def mail_gonder(self):
        mesaj = EmailMessage()
        mesaj["Subject"] = self.konu.text()
        mesaj["From"] = "seninmailin@gmail.com"
        mesaj["To"] = self.kime.text()
        mesaj.set_content(self.icerik.toPlainText())

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login("seninmailin@gmail.com", "uygulama_sifresi")
                smtp.send_message(mesaj)
            self.bilgi.setText("Mail başarıyla gönderildi.")
        except Exception as e:
            self.bilgi.setText(f"Hata: {str(e)}")

app = QApplication(sys.argv)
pencere = MailGonder()
pencere.show()
sys.exit(app.exec_())
