import random


class Dice:

    def __init__(self, type_sides: list):
        self.type_sides = type_sides

    def side_rnd(self):
        side = random.choice(self.type_sides)
        return side
