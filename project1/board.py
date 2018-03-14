import itertools
import numpy as np
import logging
logging.basicConfig(level='INFO')
def get_available_moves(board):
    x,y  = np.where(board == 0)
    
    available_x = [x]
    available_y = [y]
    x_width, y_width = np.shape(board)
    if x + 1 <= x_width - 1:
        available_x.append(x + 1)
    if x - 1  >= 0 :
        available_x.append(x - 1)
    if y + 1 <= y_width - 1:
        available_y .append(y+1)
    if y - 1  >= 0 :
        available_y.append(y-1)
    moves = filter(
        lambda m : (abs(m[0] - x) + abs(m[1] - y )) == 1,
        (itertools.product(available_x, available_y))
    )
    moves = list(moves)
    logging.debug("available moves %s", len(moves))
    return moves

def get_neighbours(node):
    successor = []
    for move in  get_available_moves(node.board):
        x = node.board.copy()
        x[ x == 0 ], x[move] = x[move], x[x==0]
        yield  Node(x, node)

def is_answer(node):

    board = node.board
    return all(board.flatten() == list(range(0,9))) or all(board.flatten() == list(range(1,9)) + [0])
    

class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
    def __eq__(self, rhs):
        return self.board.tolist() == rhs.board.tolist()

def __create_board():
    n = np.arange(9)
    np.random.shuffle(n)
    return np.reshape(n,[3,3])
if __name__ == "__main__":
    import numpy as np
    
    nroot = __create_board()
    nroot = Node(nroot)
    n1 = Node(__create_board(), nroot)
    n2 = Node(__create_board(), __create_board())
    assert (n2 in [n1, n2]) is True
    print(n1.board)

