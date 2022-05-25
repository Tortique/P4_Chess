import os
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
        tournamentName = self.view.get_tournament()
        for element in self.tournamentController.tournamentList:
            if element.name == tournamentName:
                tournament = element
                print(tournament.players)
                print("Hello")
                break
            else:
                clear()
                self.view.not_found()
                self.mainController.reports_menu()
