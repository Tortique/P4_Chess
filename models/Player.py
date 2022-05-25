class Player:
    def __init__(self, name, firstname, birthdate, gender, ranking):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = 0

    def add_ranking(self, rank):
        self.ranking = rank

    def get_ranking(self):
        return self.ranking

    def add_score(self,score):
        self.score = score

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.name} {self.firstname} {self.ranking} {self.score}"

    def __repr__(self):
        """print"""
        return str(self)