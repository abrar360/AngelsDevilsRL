# AngelsDevilsRL
A Reinforcement Learning approach to Conway's Angel Problem (except played on a 9x9 grid instead of an an infinite one)

Governor's Honors Program 2017 Mathematics Project: Abrar Ahmed and Yi Liu

Training:

Two different Reinforcement Learning algorithms are implemented:

  Q-Learning: An adjacency matrix is constructed representing the possible positions and moves on the board. Reward values are added to strategic positions on the board to establish the reward matrix R. The Q matrix is then trained iteratively according to the equation: Q(state, action) = R(state, action) + Gamma * Max[Q(next state, all actions)]. Where gamma is a learning parameter between 0 and 1.

  Feedforward Neural Network: An angel player and devil player take turns making random moves. If the game results in a loss for the angel, the neural network is penalized for each move the angel made during that game. Similarly, the neural network is rewarded for each move the angel made if the game results in a win for the angel.

Approaches have not been integrated, please see [Yi's GitHub] (https://github.com/yiliu77) for neural network agent


Decision Making:

  At any position, the angel can have a maximum of 4 possible moves (up, down, left, right). The angel agent chooses the optimum move that maximizes the reward, while taking into account squares blocked by the devil agent.
