from datetime import datetime


class Tournament:
    def __init__(self, name, location, timer):
        self.name = name
        self.location = location
        self.date = datetime.today().date()
        self.turnsNumber = 4
        self.rounds = []
        self.players = []
        self.timer = timer
        self.description = ""

    def add_date(self, date):
        """Ajoute une date"""
        self.date = date

    def add_round(self, round):
        """Ajoute un tour"""
        self.rounds.append(round)

    def add_player(self, player):
        """Ajoute un joueur"""
        self.players.append(player)

    def add_description(self, description):
        """Ajoute une description"""
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.location} {self.date}, {self.players}, {self.rounds}, {self.timer}"

    def __repr__(self):
        """print"""
        return str(self)

