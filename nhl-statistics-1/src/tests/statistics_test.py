import unittest
from statistics import Statistics
from statistics import sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4,  12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase): 
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_haku_loytaa_pelaajan(self):
        pelaaja = str(self.statistics.search("Gretzky"))
        self.assertAlmostEqual(pelaaja, "Gretzky EDM 35 + 89 = 124")

    def test_haku_ei_loyda_pelaajaa(self):
        pelaaja = self.statistics.search("Selanne")
        self.assertAlmostEqual(pelaaja, None)

    def test_listaa_joukkueen_pelaajat(self):
        pelaajat = [str(i) for i in self.statistics.team("EDM")]
        oikeat_pelaajat = [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124"
        ]
        self.assertListEqual(pelaajat, oikeat_pelaajat)

    def test_listaa_eniten_pisteita_tehneet(self):
        pelaajat = [str(i) for i in self.statistics.top_scorers(2)]
        oikeat_pelaajat = [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98"
        ]
        self.assertListEqual(pelaajat, oikeat_pelaajat)