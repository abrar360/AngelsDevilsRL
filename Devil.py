from NeuralNetwork import NeuralNetwork
import numpy as np


class Devil:
    def __init__(self, sides, trained):
        self.blocks = []
        self.sides = sides

    def get_blocks(self):
        return self.blocks

    def reset(self):
        self.blocks = []

    def god_place(self, place):
        self.blocks.append(place)

    def place_block(self, board):
        turn = np.argmax(self.consciousness.query(board))
        self.blocks.append(turn)
        return

