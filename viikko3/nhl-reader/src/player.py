class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists

    def __str__(self):
        return f"{self.name:25} {self.team:>3} {str(self.goals):>3} + {str(self.assists):>3} = {str(self.goals+self.assists):>3}"
