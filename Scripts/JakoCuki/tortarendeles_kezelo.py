# többmindent is lehet csinálni:
#   AKCIOK
#       rendelés hozzáadása
#       rendelés visszavonása
#       rednelés módosítása
#   MEGTEKINTES
#       lista az osszes rendelesrol, tobb nezet, filterek, kereses nev/torta alapjan
from rendeles import Rendeles

rendelesek = []


def uj_rendeles():
    rendelo_neve = input("Megrendelo neve: ")
    datum = input("Datum: ")
    darabszam = int(input("Mennyit tortát? "))
    rendeles = Rendeles(rendelo_neve, datum, darabszam)

    global rendelesek
    rendelesek.append(rendeles)

    print("Rendéles hozzáadva!")


def rendeles_visszavonasa():
    print("Rendelés törlése a megrendelő neve alapján!")
    megadott_nev = input("Megrendelo neve: ")
    for rendeles in rendelesek:
        if rendeles.rendelo_neve == megadott_nev:
            rendelesek.remove(rendeles)
            print(f"{megadott_nev} rendelése törölve!")


def rendeles_modositasa():
    pass


def megtekintes():
    print(f"RENDELÉSEK ({len(rendelesek)})")
    for rendeles in rendelesek:
        for torta in rendeles.tortak:
            print(torta.nev)


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
