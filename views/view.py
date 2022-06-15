from models.Player import Player


class View:

    @staticmethod
    def choice_main_menu():
        print("-Menu Principal-")
        print("Choississez une option :")
        print("1 - Tournoi")
        print("2 - Joueurs")
        print("3 - Rapports")
        print("4 - Quitter")
        print("-----------")
        return input("Choix : ")

    @staticmethod
    def choice_tournament_menu():
        print("-Menu Tournoi-")
        print("Choississez une option :")
        print("1 - Créer un tournoi")
        print("2 - Reprendre un tournoi")
        print("3 - Vider BDD")
        print("4 - Retour")
        print("-----------")
        return input("Choix : ")

    @staticmethod
    def choice_players_menu():
        print("-Menu Joueurs-")
        print("Choississez une option :")
        print("1 - Modifier le rang d'un joueur")
        print("2 - Retour")
        print("-----------")
        return input("Choix : ")

    @staticmethod
    def choice_reports_menu():
        print("-Menu Rapports-")
        print("Choississez une option :")
        print("1 - Liste des joueurs par ordre alphabétique")
        print("2 - Liste des joueurs par ordre de rang")
        print("3 - Liste des joueurs d'un tournoi par ordre alphabétique")
        print("4 - Liste des joueurs d'un tournoi par ordre de rang")
        print("5 - Liste des tournois")
        print("6 - Liste des rounds d'un tournoi")
        print("7 - Liste des matchs d'un tournoi")
        print("8 - Retour")
        print("-----------")
        return input("Choix : ")

    @staticmethod
    def name_of_tournament():
        name = input("Nom du tournoi : ")
        return name

    @staticmethod
    def location():
        location = input("Lieu : ")
        return location

    @staticmethod
    def timer():
        timer = input("Contrôle du temps : ")
        return timer

    @staticmethod
    def player(number):
        print("Ajouter Joueur ", number, ":")
        name_player = input("Nom : ")
        firstname_player = input("Prénom : ")
        birthdate = input("Date de naissance : ")
        gender = input("Genre : ")
        while True:
            try:
                ranking = int(input("Rang : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre")
        player = Player(name_player, firstname_player, birthdate, gender, ranking)
        return player

    @staticmethod
    def start_tournament():
        return input("Commencer le tournoi ? (Oui/Non) : ")

    @staticmethod
    def continue_tournament():
        return input("Continuer le tournoi ? (Oui/Non) : ")

    @staticmethod
    def show_round1(name, players):
        print(name)
        print(players[0], "vs", players[4])
        print(players[1], "vs", players[5])
        print(players[2], "vs", players[6])
        print(players[3], "vs", players[7])

    @staticmethod
    def show_round(nameOfRound, currentRound):
        print(nameOfRound)
        print(currentRound[0], "vs", currentRound[1])
        print(currentRound[2], "vs", currentRound[3])
        print(currentRound[4], "vs", currentRound[5])
        print(currentRound[6], "vs", currentRound[7])

    @staticmethod
    def finish_round(round):
        print(round)

    @staticmethod
    def show_game(player1, player2):
        print(player1, "vs", player2)

    @staticmethod
    def get_score(player1, player2):
        print("Score de ", player1, ": ")
        score1 = int(input())
        print("Score de ", player2, ": ")
        score2 = int(input())
        return [score1, score2]

    @staticmethod
    def get_tournament_name():
        return input("Quel est le nom du tournoi ? :")

    @staticmethod
    def empty_list():
        print("Aucun Tournoi enregistré")
        print("------------------------")

    @staticmethod
    def not_found():
        print("Tournoi non trouvé")
        print("------------------")

    @staticmethod
    def player_not_found():
        print("Joueur non trouvé")
        print("------------------")

    @staticmethod
    def get_tournament_date():
        return input("Date du tournoi (AAAA-MM-JJ) :")

    @staticmethod
    def get_player_name():
        return input("Nom du joueur : ")

    @staticmethod
    def get_player_firstname():
        return input("Prénom du joueur : ")

    @staticmethod
    def get_player_birthdate():
        return input("Date de naissance du joueur : ")

    @staticmethod
    def get_rank():
        return input("Quel rang voulez-vous lui attribuer ? : ")
