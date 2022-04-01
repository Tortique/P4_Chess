from models.game import Game
from models.player import Player
from models.round import Round
from models.tournament import Tournament

player = Player("Jean", "Dupont", "28/01/2022", "M")
player2 = Player("Jeanne", "Dupont", "28/01/2022", "M")
tournament = Tournament("Tournoi", "Tours", "Blitz")
round1 = Round("round 1")
game = Game(player, player2)
round1.add_game(game)

tournament.add_player(player)
tournament.add_player(player2)
tournament.add_round(round1)

print(tournament)
