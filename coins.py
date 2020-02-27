import random
class Pound:

    def __init__(self, rare = False):
        self.rare = rare
        if (self.rare == True):
            self.value = 1.5
        else:
            self.value = 1.0
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5
        self.thickness = 3.15
        self.heads = True

    def rust(self):
        self.color = "greenish"
        
    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, Falsce]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin spent!")
