class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_deuce_message(self):
        message = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All", 3: "Forty-All"}
        if self.m_score1 in message:
            return message[self.m_score1]
        return "Deuce"

    def get_advantage_message(self):
        if self.m_score1 > self.m_score2:
            return "Advantage player1"
        return "Advantage player2"

    def get_win_message(self):
        if self.m_score1 > self.m_score2:
            return "Win for player1"
        return "Win for player2"

    def get_lower_points_message(self):
        message = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return message[self.m_score1] + "-" + message[self.m_score2]

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_deuce_message()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            if abs(self.m_score1 - self.m_score2) == 1:
                return self.get_advantage_message()
            else:
                return self.get_win_message()
        return self.get_lower_points_message()
