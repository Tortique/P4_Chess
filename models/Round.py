from datetime import datetime


class Round:
    def __init__(self, name):
        now = datetime.today()
        self.name = name
        self.games = []
        self.startDate = f"{now.date().strftime('%d/%m/%y')} {now.time().isoformat(timespec='minutes')}"
        self.endDate = ""

    def end_round(self):
        now = datetime.today()
        self.endDate = f"{now.date()} {now.time().isoformat(timespec='minutes')}"

    def add_game(self, game):
        self.games.append(game)

    def __str__(self):
        return f"{self.name}, {self.startDate}, {self.endDate}, {self.games}"

    def __repr__(self):
        """print"""
        return str(self)
