from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from game_mode import GameMode

def main():
    tekoaly = Tekoaly()
    tekoaly_parannettu = TekoalyParannettu(10)
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        vastaus = input()
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )
        if vastaus.endswith("a"):
            peli = GameMode.player_vs_player()
        elif vastaus.endswith("b"):
            peli = GameMode.player_vs_ai(tekoaly)
        elif vastaus.endswith("c"):
            peli = GameMode.player_vs_better_ai(tekoaly_parannettu)
        else:
            break
        peli.pelaa()

if __name__ == "__main__":
    main()
