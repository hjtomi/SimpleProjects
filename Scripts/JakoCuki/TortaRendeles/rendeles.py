from torta import Torta


class Rendeles:
    def __init__(self, rendelo_neve, datum, **kwargs):
        self.rendelo_neve = rendelo_neve
        self.datum = datum

        self.tortak = []
        for key, value in kwargs.items():
            if key == "darabszam":
                for _ in range(value):
                    self.torta_hozzaadasa()

            elif key == "torta":
                self.tortak.append(value.__dict__)

    def torta_hozzaadasa(self):
        # torta =
        nev = input("Torta neve: ")
        meret = input("Torta merete: ")
        extra_igeny = input("Extra igenyek: ")
        self.tortak.append(Torta(nev, meret, extra_igeny).__dict__)



