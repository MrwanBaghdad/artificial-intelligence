import board as bface
import numpy as np 
from board import Node
from collections import deque


def solution_trace(answer_node):
    trace = []
    n = answer_node
    while n is not None:
        trace.append(n)
        n = n.parent
    return list(reversed(trace))

def bfs(board):
    root = Node(board)
    frontier = deque(root)
    visited = list()

    if bface.is_answer(root):
        return solution_trace(root)

    while len(frontier) > 0:
        cur = frontier.popleft()
        if cur not in visited:
            visited.append(cur)

        for n in bface.get_neighbours(cur):
            if bface.is_answer(n):
                solution_trace(n)
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
        # TODO: equality by children not whole node
        if cur not in visited : visited.append(cur)
        for n in bface.get_neighbours(cur):
            if bface.is_answer(n):
                return solution_trace(n)
            if n not in frontier and n not in visited:
                frontier.append(n)
    return None

def astar(board, heuritic):
    root = Node(board)
    

board = np.arange(9) 
board = np.random.shuffle(board) 
board = np.reshape(board,[3,3])
