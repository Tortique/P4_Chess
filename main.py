from controllers.MainController import MainController
from controllers.PlayerController import PlayerController
from controllers.ReportsController import ReportsController
from controllers.TournamentController import TournamentController
from views.view import View


def main():
    view = View()
    reportsController = ReportsController()
    tournamentController = TournamentController(reportsController)
    playerController = PlayerController(reportsController, tournamentController)
    mainController = MainController(view, tournamentController, reportsController, playerController)
    mainController.main_menu()


main()
