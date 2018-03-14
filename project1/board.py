import itertools
import numpy as np

def get_available_moves(board):
    x,y  = np.where(board)
    available_x = [] 
    available_y = []
    x_width, y_width = np.shape(board)
    if x + 1 <= x_width:
        available_x.insert(x + 1)
    if x - 1  >= 0 :
        available_x.insert(x - 1)
    if y + 1 <= y_width:
        available_y .insert(y+1)
    if y - 1  >= 0 :
        available_y.insert(y-1)
    return list(itertools.product(available_x, available_y))

def get_neighbours(node):
    for move in  get_available_moves(node.board):
        x = node.board.copy()
        x[ x == 0 ], x[move] = x[move], x[x==0]
        yield  Node(x, node)

def is_answer(node):
    board = node.board
    all(board.flatten() == np.reshape(np.arange(9),[3,3]))
    

class Node:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent