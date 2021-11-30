class Nollaus:
    def __init__(self, sovelluslogiikka, lue_aiempi):
        self._sovelluslogiikka = sovelluslogiikka
        self.lue_aiempi = lue_aiempi

    def suorita(self):
        self._aiempi = self.lue_aiempi()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.tulos = self._aiempi