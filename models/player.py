class Player:
    def __init__(self, name, firstname, birthdate, gender):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ""

    def __str__(self):
        return f"{self.name} {self.firstname}"

    def __repr__(self):
        """print"""
        return str(self)
