from controllers.PlayerController import PlayerController
from models.Game import Game
from models.Player import Player
from models.Round import Round
from models.Tournament import Tournament
from views.view import View
from controllers.MainController import MainController
from tinydb import TinyDB, Query
from controllers.Database import serializer_players, insert_players, serializer_tournament, insert_tournament, \
    deserializer_tournament, update_round, drop_tournaments
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class TournamentController:

    def __init__(self, reportController):
        self.view = View()
        self.reportsController = reportController
        self.playerController = PlayerController(reportController, self)
        self.mainController = MainController(self.view, self, self.reportsController, self.playerController)

    def new_tournament(self):
        name = self.view.name_of_tournament()
        location = self.view.location()
        timer = self.view.timer()
        tournament = Tournament(name, location, timer)
        while len(tournament.players) < 8:
            player = self.view.player(len(tournament.players) + 1)
            serialized = serializer_players(player)
            insert_players(serialized)
            tournament.add_player(player)
        serialized = serializer_tournament(tournament)
        insert_tournament(serialized)
        start = ""
        while start != "Oui" and start != "Non":
            start = self.view.start_tournament()
            if start == "Oui":
                self.start_tournament(tournament)
            elif start == "Non":
                clear()
                self.mainController.tournament_menu()

    def start_tournament(self, tournament):
        if len(tournament.rounds) == 0:
            self.first_round(tournament)
            self.ask_continue()
        while len(tournament.rounds) < 4:
            self.play_round(tournament)
            self.ask_continue()
        clear()
        self.mainController.tournament_menu()

    def ask_continue(self):
        continue_tournament = ""
        while continue_tournament != "Oui" and continue_tournament != "Non":
            continue_tournament = self.view.continue_tournament()
            if continue_tournament == "Non":
                clear()
                self.mainController.tournament_menu()

    def continue_tournament(self):
        name = self.view.get_tournament_name()
        date = self.view.get_tournament_date()
        db = TinyDB('db.json')
        tournaments = db.table('tournaments')
        TournamentDB = Query()
        count = tournaments.count(TournamentDB.name == str(name))
        if count > 0:
            tournament = deserializer_tournament(tournaments.get((TournamentDB.name == str(name)) &
                                                                 (TournamentDB.date == str(date))))
            self.start_tournament(tournament)
        else:
            clear()
            self.view.not_found()
            self.mainController.tournament_menu()

    def first_round(self, tournament):
        round = Round("Round 1")
        players = self.sort_players_by_rank(tournament)
        self.view.show_round1(round.name, players)
        superiorList = players[0:4]
        inferiorList = players[4:8]
        for player in range(len(superiorList)):
            self.view.show_game(superiorList[0], inferiorList[0])
            score = self.view.get_score(superiorList[0], inferiorList[0])
            game = Game(superiorList[0], inferiorList[0], score[0], score[1])
            round.add_game(game)
            del superiorList[0]
            del inferiorList[0]
        round.end_round()
        tournament.add_round(round)
        update_round(tournament)
        self.view.finish_round(round)

    def play_round(self, tournament):
        players_temp = []
        nameOfRound = "Round " + str(len(tournament.rounds) + 1)
        round = Round(nameOfRound)
        for p in self.sort_player_by_score_and_rank(tournament):
            players_temp.append(p)
        currentRound = []
        while len(players_temp) > 0:
            players_already_played_temp = []
            for r in tournament.rounds:
                for game in r.games:
                    if len(players_temp) == 0:
                        break
                    if players_temp[0] == game.get_player1():
                        players_already_played_temp.append(game.get_player2())
                    if players_temp[0] == game.get_player2():
                        players_already_played_temp.append(game.get_player1())
            for player in players_temp:
                if player == players_temp[0]:
                    continue
                if player in players_already_played_temp:
                    continue
                else:
                    currentRound.append(players_temp[0])
                    currentRound.append(player)
                    del players_temp[0]
                    players_temp.remove(player)
                    players_already_played_temp.clear()
                    break
        self.view.show_round(nameOfRound, currentRound)
        while len(currentRound) > 0:
            self.view.show_game(currentRound[0], currentRound[1])
            score = self.view.get_score(currentRound[0], currentRound[1])
            game = Game(currentRound[0], currentRound[1], score[0], score[1])
            round.add_game(game)
            del currentRound[0]
            del currentRound[0]
        round.end_round()
        tournament.add_round(round)
        update_round(tournament)
        self.view.finish_round(round)

    @staticmethod
    def sort_players_by_rank(tournament):
        players = tournament.players
        players.sort(key=Player.get_ranking)
        return players

    @staticmethod
    def sort_player_by_score_and_rank(tournament):
        players = tournament.players
        for player in players:
            score = 0
            for round in tournament.rounds:
                for game in round.games:
                    if player == game.get_player1():
                        score += game.get_score1()
                    elif player == game.get_player2():
                        score += game.get_score2()
            player.add_score(score)
        players.sort(key=Player.get_score, reverse=True)
        return players

    def del_tournaments(self):
        drop_tournaments()
        self.mainController.tournament_menu()
