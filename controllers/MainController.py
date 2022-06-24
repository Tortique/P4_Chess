import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class MainController:

    def __init__(self, view, tournamentController, reportsController, playerController):
        self.view = view
        self.tournamentController = tournamentController
        self.reportsController = reportsController
        self.playerController = playerController
        self.mainMenu = {
            '1': self.tournament_menu,
            '2': self.players_menu,
            '3': self.reports_menu,
            '4': quit
        }
        self.tournamentMenu = {
            '1': self.tournamentController.new_tournament,
            '2': self.tournamentController.continue_tournament,
            '3': self.tournamentController.del_tournaments,
            '4': self.main_menu
        }
        self.playersMenu = {
            '1': self.playerController.change_player_ranking,
            '2': self.main_menu
        }
        self.reportsMenu = {
            '1': self.reportsController.get_all_players_by_alphabetical,
            '2': self.reportsController.get_all_players_by_rank,
            '3': self.reportsController.get_report_tournament_players_by_alphabetical,
            '4': self.reportsController.get_report_tournament_players_by_rank,
            '5': self.reportsController.get_all_tournaments,
            '6': self.reportsController.get_all_rounds_of_tournament,
            '7': self.reportsController.get_all_games_of_tournament,
            '8': self.main_menu
        }

    def main_menu(self):
        choice = 0
        while choice not in ['1', '2', '3', '4']:
            choice = self.view.choice_main_menu()
            action = self.mainMenu.get(choice)
            if action:
                clear()
                action()
            else:
                clear()
                print("{0} n'est pas un choix possible".format(choice))
                print("-------------------------------")

    def tournament_menu(self):
        choice = 0
        while choice not in ['1', '2', '3', '4']:
            choice = self.view.choice_tournament_menu()
            action = self.tournamentMenu.get(choice)
            if action:
                clear()
                action()
            else:
                clear()
                print("{0} n'est pas un choix possible".format(choice))
                print("-------------------------------")

    def players_menu(self):
        choice = 0
        while choice not in ['1', '2']:
            choice = self.view.choice_players_menu()
            action = self.playersMenu.get(choice)
            if action:
                clear()
                action()
            else:
                clear()
                print("{0} n'est pas un choix possible".format(choice))
                print("-------------------------------")

    def reports_menu(self):
        choice = 0
        while choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            choice = self.view.choice_reports_menu()
            action = self.reportsMenu.get(choice)
            if action:
                clear()
                action()
            else:
                clear()
                print("{0} n'est pas un choix possible".format(choice))
                print("-------------------------------")
