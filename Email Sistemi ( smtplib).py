# Bu Python dosyası, bir dosyadan isim ve e-posta adreslerini okuyarak her kişiye bir e-posta gönderir.
import smtplib
from email.message import EmailMessage

def mail_gonder(isim, email):
    mesaj = EmailMessage()
    mesaj["Subject"] = "Projeden Selamlar!"
    mesaj["From"] = "seninmailin@gmail.com"
    mesaj["To"] = email
    mesaj.set_content(f"Merhaba {isim}, bu bir test mailidir. :)")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("seninmailin@gmail.com", "uygulama_sifresi")
        smtp.send_message(mesaj)

with open("kisiler.txt", "r", encoding="utf-8") as f:
    for satir in f:
        if satir.strip():
            isim, email = satir.strip().split(",")
            mail_gonder(isim, email)
            print(f"{isim} kişisine mail gönderildi.")
