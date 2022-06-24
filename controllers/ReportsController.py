import os

from tinydb import TinyDB, Query

from controllers.Database import deserializer_tournament, deserializer_players
from controllers.MainController import MainController
from controllers.PlayerController import PlayerController
from controllers.TournamentController import TournamentController
from models.Player import Player
from views.view import View


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class ReportsController:

    def __init__(self):
        self.view = View()
        self.tournamentController = TournamentController(self)
        self.playerController = PlayerController(self, self.tournamentController)
        self.mainController = MainController(self.view, self.tournamentController, self, self.playerController)
        self.db = TinyDB('db.json')
        self.tournaments = self.db.table('tournaments')
        self.players = self.db.table('players')

    def get_all_players_by_alphabetical(self):
        clear()
        playersList = []
        players = self.players.all()
        for player in players:
            playersList.append(deserializer_players(player))
        playersList.sort(key=Player.get_name)
        for player in playersList:
            player.get_player_infos()

    def get_all_players_by_rank(self):
        clear()
        playersList = []
        players = self.players.all()
        for player in players:
            playersList.append(deserializer_players(player))
        playersList.sort(key=Player.get_ranking)
        for player in playersList:
            player.get_player_infos()

    def get_report_tournament_players_by_alphabetical(self):
        clear()
        TournamentDB = Query()
        tournamentName = self.view.get_tournament_name()
        tournamentDate = self.view.get_tournament_date()
        count = self.tournaments.count((TournamentDB.name == str(tournamentName)) &
                                       (TournamentDB.date == str(tournamentDate)))
        if count > 0:
            tournament = deserializer_tournament(self.tournaments.get((TournamentDB.name == str(tournamentName)) &
                                                                      (TournamentDB.date == str(tournamentDate))))
            tournament.players.sort(key=Player.get_name)
            for player in tournament.players:
                player.get_player_in_tournament()
        else:
            clear()
            self.view.not_found()
            self.mainController.reports_menu()

    def get_report_tournament_players_by_rank(self):
        clear()
        TournamentDB = Query()
        tournamentName = self.view.get_tournament_name()
        tournamentDate = self.view.get_tournament_date()
        count = self.tournaments.count((TournamentDB.name == str(tournamentName)) &
                                       (TournamentDB.date == str(tournamentDate)))
        if count > 0:
            tournament = deserializer_tournament(self.tournaments.get((TournamentDB.name == str(tournamentName)) &
                                                                      (TournamentDB.date == str(tournamentDate))))
            tournament.players.sort(key=Player.get_ranking)
            for player in tournament.players:
                player.get_player_in_tournament()
        else:
            clear()
            self.view.not_found()
            self.mainController.reports_menu()

    def get_all_tournaments(self):
        clear()
        tournaments = self.tournaments.all()
        for tournament in tournaments:
            print(deserializer_tournament(tournament))

    def get_all_rounds_of_tournament(self):
        clear()
        TournamentDB = Query()
        tournamentName = self.view.get_tournament_name()
        tournamentDate = self.view.get_tournament_date()
        count = self.tournaments.count(TournamentDB.name == str(tournamentName))
        if count > 0:
            tournament = deserializer_tournament(self.tournaments.get((TournamentDB.name == str(tournamentName)) &
                                                                      (TournamentDB.date == str(tournamentDate))))
            tournament.show_rounds()
        else:
            clear()
            self.view.not_found()
            self.mainController.reports_menu()

    def get_all_games_of_tournament(self):
        clear()
        TournamentDB = Query()
        tournamentName = self.view.get_tournament_name()
        tournamentDate = self.view.get_tournament_date()
        count = self.tournaments.count(TournamentDB.name == str(tournamentName))
        if count > 0:
            tournament = deserializer_tournament(self.tournaments.get((TournamentDB.name == str(tournamentName)) &
                                                                      (TournamentDB.date == str(tournamentDate))))
            tournament.show_games()
        else:
            clear()
            self.view.not_found()
            self.mainController.reports_menu()
