from controllers.MainController import MainController
from controllers.ReportsController import ReportsController
from controllers.TournamentController import TournamentController
from views.view import View


def main():
    view = View()
    reportsController = ReportsController()
    tournamentController = TournamentController(reportsController)
    mainController = MainController(view, tournamentController, reportsController)
    mainController.main_menu()


main()
