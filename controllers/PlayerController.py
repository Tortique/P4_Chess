import os

from tinydb import TinyDB, Query

from controllers.Database import deserializer_players
from controllers.MainController import MainController
from views.view import View


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class PlayerController:
    def __init__(self, reportsController, tournamentController):
        self.view = View()
        self.reportsController = reportsController
        self.tournamentController = tournamentController
        self.mainController = MainController(self.view, self.tournamentController, self.reportsController, self)
        self.db = TinyDB('db.json')
        self.players = self.db.table('players')

    def change_player_ranking(self):
        clear()
        playerName = self.view.get_player_name()
        playerFirstname = self.view.get_player_firstname()
        playerBirthdate = self.view.get_player_birthdate()
        playerRank = self.view.get_rank()
        PlayerDB = Query()
        count = self.players.count((PlayerDB.name == str(playerName)) &
                                   (PlayerDB.firstname == str(playerFirstname)) &
                                   (PlayerDB.birthdate == str(playerBirthdate)))
        if count > 0:
            self.players.update({'ranking': playerRank}, (PlayerDB.name == str(playerName)) &
                                (PlayerDB.firstname == str(playerFirstname)) &
                                (PlayerDB.birthdate == str(playerBirthdate)))
            player = deserializer_players(self.players.get((PlayerDB.name == str(playerName)) &
                                      (PlayerDB.firstname == str(playerFirstname)) &
                                      (PlayerDB.birthdate == str(playerBirthdate))))
            player.get_player_infos()
        else:
            clear()
            self.view.player_not_found()
            self.mainController.players_menu()
