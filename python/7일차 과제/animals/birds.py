# animals/birds.py

class Eagle:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def fly(self):
        return "Eagle is flying!"

    def info(self):
        return f"{self.name} is an {self.species}."