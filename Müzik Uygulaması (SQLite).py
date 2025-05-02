#Bu proje sqlite3 kullanarak bir şarkı veritabanı oluşturmayı ve şarkı ekleme, silme ve toplam süre hesaplama işlevlerini içermektedir.
import sqlite3

conn = sqlite3.connect("sarki_projesi.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sarkilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isim TEXT,
    sanatci TEXT,
    album TEXT,
    prod_sirketi TEXT,
    sure INTEGER  -- saniye cinsinden
)
""")
conn.commit()

def sarki_ekle(isim, sanatci, album, prod_sirketi, sure):
    cursor.execute("""
    INSERT INTO sarkilar (isim, sanatci, album, prod_sirketi, sure)
    VALUES (?, ?, ?, ?, ?)
    """, (isim, sanatci, album, prod_sirketi, sure))
    conn.commit()

def sarki_sil(sarki_id):
    cursor.execute("DELETE FROM sarkilar WHERE id = ?", (sarki_id,))
    conn.commit()

def toplam_sure():
    cursor.execute("SELECT SUM(sure) FROM sarkilar")
    total = cursor.fetchone()[0]
    if total is None:
        return 0
    return total

sarki_ekle("Haydi Gel İçelim", "Müslüm Gürses", "Altın Klasikler", "Arabesk Prod.", 210)
sarki_ekle("Beni Bırakma", "Tarkan", "Yandım", "Mega Müzik", 195)

print("Toplam süre (saniye):", toplam_sure())

conn.close()
