import json

from tinydb import TinyDB

from models.Player import Player
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
    players_table.insert(serialized_player)

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
        serialized_tournament['rounds'].append(round)
    return serialized_tournament


def insert_tournament(serialized_tournament):
    db = TinyDB('db.json')
    tournaments_table = db.table('tournaments')
    tournaments_table.insert(serialized_tournament)


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
    tournament.rounds = rounds
    tournament.add_date(date)
    tournament.add_description(description)
    return tournament
