from tinydb import TinyDB, Query

from models.Game import Game
from models.Player import Player
from models.Round import Round
from models.Tournament import Tournament


def serializer_players(player):
    serialized_player = {
        'name': player.name,
        'firstname': player.firstname,
        'birthdate': player.birthdate,
        'gender': player.gender,
        'ranking': player.ranking,
        'score': player.score
    }
    return serialized_player


def insert_players(serialized_player):
    db = TinyDB('db.json')
    players_table = db.table('players')
    PlayerDB = Query()
    players_table.upsert(serialized_player, (PlayerDB.name == str(serialized_player['name'])) &
                         (PlayerDB.firstname == str(serialized_player['firstname'])) &
                         (PlayerDB.birthdate == str(serialized_player['birthdate'])))


def deserializer_players(player):
    name = player['name']
    firstname = player['firstname']
    birthdate = ['birthdate']
    gender = player['gender']
    ranking = player['ranking']
    score = player['score']
    player = Player(name, firstname, birthdate, gender, ranking)
    player.add_score(score)
    return player


def serializer_rounds(round):
    serialized_round = {
        'name': round.name,
        'games': [],
        'startDate': round.startDate,
        'endDate': round.endDate
    }
    for game in round.games:
        serialized_round['games'].append(serializer_games(game))
    return serialized_round


def deserializer_rounds(round):
    name = round['name']
    games = round['games']
    startDate = round['startDate']
    endDate = round['endDate']
    round = Round(name)
    round.change_start_date(startDate)
    round.change_end_date(endDate)
    for game in games:
        round.add_game(deserializer_games(game))
    return round


def serializer_games(game):
    serialized_game = {
        'player1': serializer_players(game.get_player1()),
        'score1': game.get_score1(),
        'player2': serializer_players(game.get_player2()),
        'score2': game.get_score2()
    }
    return serialized_game


def deserializer_games(game):
    player1 = deserializer_players(game['player1'])
    score1 = game['score1']
    player2 = deserializer_players(game['player2'])
    score2 = game['score2']
    game = Game(player1, player2, score1, score2)
    return game


def serializer_tournament(tournament):
    serialized_tournament = {
        'name': tournament.name,
        'location': tournament.location,
        'date': f"{tournament.date}",
        'turnNumber': tournament.turnsNumber,
        'rounds': [],
        'players': [],
        'timer': tournament.timer,
        'description': tournament.description
    }
    for player in tournament.players:
        serialized_tournament['players'].append(serializer_players(player))
    for round in tournament.rounds:
        serialized_tournament['rounds'].append(serializer_rounds(round))
    return serialized_tournament


def insert_tournament(serialized_tournament):
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.insert(serialized_tournament)


def update_round(tournament):
    db = TinyDB('db.json')
    tournament_table = db.table('tournaments')
    TournamentDB = Query()
    tournament_table.upsert(serializer_tournament(tournament), (TournamentDB.name == str(tournament.name)) &
                            (TournamentDB.date == str(tournament.date)))


def deserializer_tournament(tournament):
    name = tournament['name']
    location = tournament['location']
    date = tournament['date']
    rounds = tournament['rounds']
    players = tournament['players']
    timer = tournament['timer']
    description = ['description']
    tournament = Tournament(name, location, timer)
    for player in players:
        tournament.add_player(deserializer_players(player))
    for round in rounds:
        tournament.add_round(deserializer_rounds(round))
    tournament.add_date(date)
    tournament.add_description(description)
    return tournament


def drop_tournaments():
    db = TinyDB('db.json')
    db.drop_table("tournaments")
    db.drop_table("players")
