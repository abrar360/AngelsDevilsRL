import numpy as np
import random


# defines the reward/connection graph

class QLearn:
    def set_r(self):
        for i in range(81):
            moves = [i - 1, i + 1, i - 9, i + 9]
            for m in moves:
                if 0 <= m <= 80:
                    diff = (self.get_layer(m) - self.get_layer(i)) * 25 * self.get_layer(m)  # TWEAK THIS
                    if diff > -100000:
                        self.r[i, m] = diff
                    # else:
                    #     self.r[i, m] = 0

    def __init__(self):
        self.r = np.ones((81,81)).dot(-1)
        self.l4 = [0,1,2,3,4,5,6,7,8,17,26,35,44,53,62,71,80,79,78,77,76,75,74,73,72,63,54,45,36,27,18,9]
        self.l3 = [10,11,12,13,14,15,16,25,34,43,52,61,70,69,68,67,66,65,64,55,46,37,28,19]
        self.l2 = [20,21,22,23,24,33,42,51,60,59,58,57,56,47,38,29]
        self.l1 = [30,31,32,41,50,49,48,39]
        self.l0 = [40]
        self.gamma = 0.8
        self.q = np.zeros_like(self.r)
        self.set_r()
        self.blocked = []

    def get_layer(self, square):
        if square in self.l0:
            return 0
        elif square in self.l1:
            return 1
        elif square in self.l2:
            return 2
        elif square in self.l3:
            return 3
        elif square in self.l4: #REPLACE WITH ELSE LATER
            return 4
        else: return 20


    def update_q(self, state, gamma):
        action = np.random.choice(np.where(self.r[state] > -1)[0])
        #next_state = np.random.choice(np.where(r[state] == np.amax(r[state]))[0])
        update_max = np.amax(self.q[state])
        rsa = self.r[state, action]
        new_q = rsa + (gamma * update_max)
        self.q[state, action] = new_q
        #print(state)
        return action


    def train_q(self):
        print("Training...")
        for u in range(100000):
            if u % 10000 == 0:
                print(u)
            state = random.randint(0, 80)
            while self.get_layer(state) != 4:
                state = self.update_q(state, self.gamma)

    def get_move(self, state):
        adj = [state - 1, state + 1, state - 9, state + 9]
        pos = []
        for d in adj:
            if d not in self.blocked:
                pos.append(d)
        move = np.random.choice(np.where(self.q[state] == np.amax(self.q[state]))[0])
        if move not in pos:
            if len(pos) > 0:
                move = np.random.choice(pos)
            else:
                move = 101
        print(np.where(self.q[state] == np.amax(self.q[state])))
        print("move: " + str(move))
        return move

    def block(self, state):
        print("blocked " + str(state))
        self.q[:, state] = np.zeros_like(self.q[:, state])
        self.blocked.append(state)
