class Game:
    def __init__(self, player1, player2, score1, score2):
        player1, player2 = [player1, score1], [player2, score2]
        self.game = player1, player2

    def get_player1(self):
        return self.game[0][0]

    def get_player2(self):
        return self.game[1][0]

    def get_score1(self):
        return self.game[0][1]

    def get_score2(self):
        return self.game[1][1]

    def __str__(self):
        return f"{self.game[0][0]}, {self.game[0][1]} vs {self.game[1][0]}, {self.game[1][1]}"

    def __repr__(self):
        """print"""
        return str(self)
