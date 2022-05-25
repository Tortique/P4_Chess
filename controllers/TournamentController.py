from models.Game import Game
from models.Player import Player
from models.Round import Round
from models.Tournament import Tournament
from views.view import View
from controllers.MainController import MainController
from controllers.ReportsController import ReportsController
from tinydb import TinyDB, Query
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class TournamentController:

    def __init__(self, reportController):
        self.view = View()
        self.tournamentList = []
        self.reportsController = ReportsController()
        self.mainController = MainController(self.view, self, self.reportsController)

    def new_tournament(self):
        db = TinyDB('db.json')
        players = db.table('players')
        Players = Query()
        name = self.view.name_of_tournament()
        location = self.view.location()
        timer = self.view.timer()
        tournament = Tournament(name, location, timer)
        while len(tournament.players) < 8:
            player = self.view.player(len(tournament.players) + 1)

            tournament.players.append(player)
        self.tournamentList.append(tournament)
        start = ""
        while start != "Oui" and start != "Non":
            start = self.view.start_tournament()
            if start == "Oui":
                self.start_tournament(tournament)
            elif start == "Non":
                clear()
                self.mainController.tournament_menu()

    def start_tournament(self, tournament):
        self.first_round(tournament)
        while len(tournament.rounds) < 4:
            self.round(tournament)
        clear()
        self.mainController.tournament_menu()

    def continue_tournament(self):
        if not self.tournamentList:
            self.view.empty_list()
            self.mainController.tournament_menu()
        else:
            name = self.view.get_tournament()
            for element in self.tournamentList:
                if element.name == name:
                    tournament = element
                    print(tournament)
                    break
                else:
                    clear()
                    self.view.not_found()
                    self.mainController.tournament_menu()

    def first_round(self, tournament):
        round = Round("Round 1")
        players = self.sort_players_by_rank(tournament)
        self.view.show_round1(players)
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
        self.view.finish_round(round)

    def round(self, tournament):
        players_temp = []
        nameOfRound = "Round " + str(len(tournament.rounds) + 1)
        round = Round(nameOfRound)
        for p in self.sort_player_by_score_and_rank(tournament):
            players_temp.append(p)
        currentRound = []
        while len(players_temp) > 0:
            i = 1
            playable = True
            for r in tournament.rounds:
                for game in r.games:
                    if len(players_temp) == 0:
                        break
                    if players_temp[0] == game.get_player1() or players_temp[0] == game.get_player2():
                        if players_temp[i] == game.get_player1() or players_temp[i] == game.get_player2():
                            i = i + 1
                            playable = False
            if playable:
                currentRound.append(players_temp[0])
                currentRound.append(players_temp[i])
                del players_temp[0]
                del players_temp[i - 1]
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
