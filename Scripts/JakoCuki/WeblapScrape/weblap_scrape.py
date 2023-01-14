from bs4 import BeautifulSoup
import requests

torta_nevek = []

for i in range(1, 4):
    response = requests.get(f"https://jakocukraszda.com/kategoria/tortak/oldal/{i}/")
    response.raise_for_status()

    web_html = response.text
    soup = BeautifulSoup(web_html, "html.parser")

    torta_nevek.extend(soup.select(".product-info a"))

torta_nevek = list(map(lambda x: x.getText(), torta_nevek))
del torta_nevek[2-1::2]
print(torta_nevek)
