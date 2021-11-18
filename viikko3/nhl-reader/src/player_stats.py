from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.players = self.__create_dict(reader.response)

    def __create_dict(self, response):
        players = []
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
            )
            players.append(player)
        return players

    def top_scorers_by_nationality(self, nationality):
        result = []
        for player in self.players:
            if player.nationality == nationality:
                result.append(player)
        result.sort(key=lambda x: x.goals + x.assists, reverse=True)
        return result[:10] 
