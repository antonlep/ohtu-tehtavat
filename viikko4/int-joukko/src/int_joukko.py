class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko
        self.ljono = [None] * self.kapasiteetti

    def alkioiden_lkm(self):
        return len(self.ljono) - self.ljono.count(None)

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if not self.kuuluu(n):
            first_empty = self.ljono.index(None)
            self.ljono[first_empty] = n
            if self.alkioiden_lkm() == len(self.ljono):
                self.kasvata()
            return True
        return False

    def kasvata(self):
        self.ljono = self.ljono + [None] * self.kasvatuskoko

    def poista(self, n):
        if n in self.ljono:
            self.ljono.remove(n)
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm()

    def to_int_list(self):
        return [i for i in self.ljono if i != None]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in a_taulu + b_taulu:
            x.lisaa(i)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in a_taulu:
            if i in b_taulu:
                y.lisaa(i)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in a_taulu:
            z.lisaa(i)
        for i in b_taulu:
            z.poista(i)
        return z

    def __str__(self):
        return "{" + (', ').join(str(x) for x in self.to_int_list()) + "}"
