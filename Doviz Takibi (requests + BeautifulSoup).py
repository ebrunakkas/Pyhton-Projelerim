#Bu script, Türkiye'deki döviz kurları ve borsa bilgilerini anlık olarak almak için kullanılmaktadır.
import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

def veri_al(selector):
    veri = soup.select_one(selector)
    return veri.text.strip() if veri else "Bulunamadı"

print("🔄 Anlık Piyasa Bilgileri")
print("Dolar:", veri_al(".dovizBar .item:nth-child(1) .value"))
print("Euro:", veri_al(".dovizBar .item:nth-child(2) .value"))
print("Altın:", veri_al(".dovizBar .item:nth-child(3) .value"))
print("Borsa:", veri_al(".dovizBar .item:nth-child(5) .value"))
