class Game:
    def __init__(self, player1, player2):
        playerA = []
        playerB = []
        playerA.append(player1)
        playerB.append(player2)
        score = ""
        playerA.append(score)
        playerB.append(score)
        self.players = (playerA, playerB)

    def __str__(self):
        return f"{self.players}"

    def __repr__(self):
        """print"""
        return str(self)
