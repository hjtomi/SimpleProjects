from torta import Torta


class Rendeles:
    def __init__(self, rendelo_neve, datum, darabszam):
        self.rendelo_neve = rendelo_neve
        self.datum = datum

        self.tortak = []
        for _ in range(darabszam):
            self.torta_hozzaadasa()

    def torta_hozzaadasa(self):
        # torta =
        nev = input("Torta neve: ")
        meret = input("Torta merete: ")
        extra_igeny = input("Extra igenyek: ")
        self.tortak.append(Torta(nev, meret, extra_igeny))



