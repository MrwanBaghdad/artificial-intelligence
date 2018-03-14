import board as bface
import numpy as np 
from board import Node
from collections import deque
import time

def solution_trace(answer_node, rootNode):
    trace = []
    n = answer_node
    while n is not rootNode:
        trace.append(n.board)
        n = n.parent
    return (list(reversed(trace)))

def bfs(board):
    root = Node(board)
    frontier = deque()
    frontier.append(root)
    visited = list()
    start = time.time()
    if bface.is_answer(root):
        return solution_trace(root, root)

    while len(frontier) > 0:
        cur = frontier.popleft()
        if cur not in visited:
            visited.append(cur)
        for n in bface.get_neighbours(cur):
            if bface.is_answer(n):
                print(time.time() - start)
                return solution_trace(n, root)
            if n not in frontier and n not in visited:
                frontier.append(n)
    return None

def dfs(board):
    root = Node(board)
    frontier = list()
    visited = list()

    if bface.is_answer(root):
        return solution_trace(root)
    frontier.append(root)
    while len(frontier) > 0:
        cur = frontier.pop()
        if cur not in visited : visited.append(cur)
        for n in bface.get_neighbours(cur):
            if bface.is_answer(n):
                return solution_trace(n)
            if n not in frontier and n not in visited:
                frontier.append(n)
    return None

def astar(board, heuritic):
    root = Node(board)
    

if __name__ == "__main__":
    from board import __create_board
    
    nroot = np.reshape(
        [2, 0, 3,
         1, 4, 6,
         7, 5, 8], [3,3])
    # nroot = __create_board()
    
    from pprint import pprint
    pprint((bfs(nroot)))