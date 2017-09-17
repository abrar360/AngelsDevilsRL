from Board import Board
from QLearn import QLearn


ql = QLearn()


def get_ql():
    return ql

ql.train_q()

board = Board(60, 9, ql)
board.init_draw()

while True:
        board.display_board()
        pressed = board.god_as_devil()
        winner = board.get_winner()
        if pressed is True:
            ql.block(board.get_devil_blocks())
            board.angels_turn()
        if winner is not None:
            print("===================")
            print("Winner: " + winner)
            print("Reason: " + board.get_reason())
            print("===================")
            break

