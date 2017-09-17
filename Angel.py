import numpy as np
from NeuralNetwork import NeuralNetwork


class Angel:
    def __init__(self, sides, trained=False):
        self.sides = sides
        self.position = int(sides / 2) * sides + int(sides / 2)
        self.moves = []

    def get_last_move(self):
        if not len(self.moves) == 0:
            return self.moves[len(self.moves) - 1]

    def get_position(self):
        return self.position

    def reset(self):
        self.position = int(self.sides / 2) * self.sides + int(self.sides / 2)
        self.moves = []
        self.consciousness.reset()

 
    def angel_move(self, board, ql):
        self.position = ql.get_move(self.position)


    def train(self, has_won):
        if has_won is "devil":
            self.consciousness.train(False)
        if has_won is "angel":
            self.consciousness.train(True)


    def god_move(self, move):
        if move == -self.sides:
            self.moves.append(0)
        if move == 1:
            self.moves.append(1)
        if move == self.sides:
            self.moves.append(2)
        if move == -1:
            self.moves.append(3)
        self.position += move
