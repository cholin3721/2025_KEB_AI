class Pokemon:
    def __init__(self, name):
        self.name = name
    def walks(self):
        print("walk..")
    def attack(self, target_pokemon):
        print(f"{self.name} attack {target_pokemon.name}")

class Pikachu(Pokemon):
    pass


class Agumon:
    def __init__ (self, name):
        self.name = name
        
agumon = Agumon("Agumon")
pikachu = Pikachu("Pikachu")
pikachu.attack(agumon)


