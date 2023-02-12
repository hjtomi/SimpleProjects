# többmindent is lehet csinálni:
#   AKCIOK
#       rendelés hozzáadása
#       rendelés visszavonása
#       rednelés módosítása
#   MEGTEKINTES
#       lista az osszes rendelesrol, tobb nezet, filterek, kereses nev/torta alapjan

# Fontos hogy JSON friendly legyen a konnyu adat betoltes miatt!

# holnapra otlet: az adattarolas nem objectekben kene hanem dictionarikban, mivel csak tulajdonsagokat tarol
#       tehat reworkolni kene az egesz rendszert

from rendeles import Rendeles
from torta import Torta
import json

data_path = "rendelesek.json"

torta = Torta("karolyi", "nagy")
rendelesek_obj = [Rendeles("Tomo", "holnap", torta=torta)]

try:
    with open("data.json", "r") as file:
        data = json.load(file)

        data.update(rendelesek_obj[-1].__dict__)

except FileNotFoundError:
    with open("data.json", "w") as file:
        json.dump(rendelesek_obj[-1].__dict__, file, indent=4)

else:
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
# ?


def uj_rendeles():
    rendelo_neve = input("Megrendelo neve: ")
    datum = input("Datum: ")
    darabszam = int(input("Mennyit tortát? "))
    rendeles = Rendeles(rendelo_neve, datum, darabszam=darabszam)

    global rendelesek_obj
    rendelesek_obj.append(rendeles)

    print("Rendéles hozzáadva!")


def rendeles_visszavonasa():
    print("Rendelés törlése a megrendelő neve alapján!")
    megadott_nev = input("Megrendelo neve: ")
    global rendelesek_obj
    for rendeles in rendelesek_obj:
        if rendeles.rendelo_neve == megadott_nev:
            rendelesek_obj.remove(rendeles)
            print(f"{megadott_nev} rendelése törölve!")


def rendeles_modositasa():
    pass


def megtekintes():
    print(f"RENDELÉSEK ({len(rendelesek_obj)})")
    for rendeles in rendelesek_obj:
        print(rendeles.__dict__)


akciok_dict = {
    "A": uj_rendeles,
    "B": rendeles_visszavonasa,
    "C": rendeles_modositasa,
    "D": megtekintes
}

app_on = True
while app_on:
    dontes = input("Mit szeretnel csinalni? ").upper()
    akciok_dict[dontes]()
