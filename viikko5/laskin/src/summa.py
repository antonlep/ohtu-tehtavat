class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.arvo = 0
        try:
            self.arvo = int(self.lue_syote())
        except Exception:
            pass
        self._sovelluslogiikka.plus(self.arvo)

    def kumoa(self):
        self._sovelluslogiikka.miinus(self.arvo)