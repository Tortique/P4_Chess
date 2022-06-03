import os

from tinydb import TinyDB, Query

from controllers.Database import deserializer_tournament
from controllers.MainController import MainController
from controllers.TournamentController import TournamentController
from views.view import View


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class ReportsController:

    def __init__(self):
        self.view = View()
        self.tournamentController = TournamentController(self)
        self.mainController = MainController(self.view, self.tournamentController, self)

    def get_report_by_alphabetical(self):
        clear()
        db = TinyDB('db.json')
        tournaments = db.table('tournaments')
        TournamentDB = Query()
        tournamentName = self.view.get_tournament()
        count = tournaments.count(TournamentDB.name == str(tournamentName))
        if count > 0:
            if count == 1:
                tournament = deserializer_tournament(tournaments.get(TournamentDB.name == str(tournamentName)))
                tournament.show_players()
            if count > 1:
                date = self.view.more_than_one_tournament()
                tournament = deserializer_tournament(tournaments.get((TournamentDB.name == str(tournamentName)) &
                                                                     (TournamentDB.date == str(date))))
                tournament.show_players()
        else:
            clear()
            self.view.not_found()
            self.mainController.reports_menu()
