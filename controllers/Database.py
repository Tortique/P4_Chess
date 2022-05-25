from tinydb import TinyDB, Query


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

def get_players():

