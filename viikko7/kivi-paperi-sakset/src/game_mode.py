from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class GameMode:
    @staticmethod
    def player_vs_player():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def player_vs_ai(tekoaly):
        return KPSTekoaly(tekoaly)

    @staticmethod
    def player_vs_better_ai(parannettu_tekoaly):
        return KPSParempiTekoaly(parannettu_tekoaly)