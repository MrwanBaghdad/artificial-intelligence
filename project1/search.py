import board as bface
import numpy as np 
from board import Node
from collections import deque
import time
import logging

# logging.basicConfig(level=logging.DEBUG)
def solution_trace(answer_node, rootNode):# fuction of work includin 
    trace = []
    n = answer_node
    while n is not rootNode:
        trace.append(n.board)
        n = n.parent
    
    # print("path cost: "+str(len(trace)))
    return { "answer": list(reversed(trace)), "path cost": str(len(trace))}


def bfs(board):
    root = Node(board)
    frontier = deque()
    frontier.append(root)
    visited = list()
    start = time.time()
    if bface.is_answer(root):
        return solution_trace(root, root)

    while len(frontier)> 0:
        cur = frontier.popleft()
        if cur not in visited:
            visited.append(cur)
        for n in bface.get_neighbours(cur):
            if bface.is_answer(n):
                print(time.time() - start)
                print("number of expanded nodes"+str(len(visited)))
                return solution_trace(n, root)
            if n not in frontier and n not in visited:
                frontier.append(n)
    return None


def dfs(board):
    root = Node(board)
    frontier = list()
    visited = list()
    start_time = time.time()
    if bface.is_answer(root):
        return solution_trace(root, root)
    frontier.append(root)
    while len(frontier) > 0:
        cur = frontier.pop()
        if cur not in visited : 
            visited.append(cur)
        for n in bface.get_neighbours(cur):
            if bface.is_answer(n):
                print(time.time() - start_time)
                print("number of expanded nodes"+str(len(visited)))
                return solution_trace(n, root)
            if n not in frontier and n not in visited:
                frontier.append(n)
    return None

def astar(board, heuritic):
    from heapq import heappush, heappop, nsmallest
    start_time = time.time()
    root = Node(board)
    visited = list()
    frontier = []
    if bface.is_answer(root):
        return solution_trace(root, root)
    
    def  _heappush(node):
        heappush(frontier,
        (len(solution_trace(node, root)) + heuritic(node.board),node))
    
    _heappush(root)
    # cur = heappop(frontier)[1]
    while len(frontier) > 0:
        cur = heappop(frontier)
        cur = cur[1]
        if bface.is_answer(cur):
            print(time.time() - start_time)
            print("number of expanded nodes",str(len(visited)))
            print("...")
            return solution_trace(cur, root)
        visited.append(cur)
        for n in bface.get_neighbours(cur):
            if n not in visited and n not in frontier:
                _heappush(n)
            elif n in frontier:
                frontier.remove(n)
                n.parent = cur
                _heappush(n)

def manhattan_distance(board):
    dist = 0
    for (x, y) , value in np.ndenumerate(board):
        xsolution, ysolution = np.where(bface.answer_board == value)
        dist += abs(x - xsolution) + abs(y - ysolution)
    return dist/2

def euclidian_distance(board):
    dist = 0
    for (x, y) , value in np.ndenumerate(board):
        xsolution, ysolution = np.where(bface.answer_board == value)
        dist += (x - xsolution)**2 + (y - ysolution)**2
        dist = np.sqrt(dist)
    return dist



if __name__ == "__main__":
    from board import __create_board
    nroot = np.reshape(
        [1, 2, 5,
         3, 0, 4,
         6, 7, 8], [3,3])
    # nroot = __create_board()
    from pprint import pprint
    #testing dfs and bfs
    # pprint((dfs(nroot)))
    print("BFS")
    pprint(bfs(nroot))
    
    print("DFS")
    pprint(dfs(np.reshape(
        [1,2,3,4,5,6,7,0,8],
        [3,3]
    )))
    
    #testing heursistic 
    
    print("Astar manhatan")
    pprint(astar(nroot, manhattan_distance))
    
    print("Astart with euclidian distance")
    pprint(astar(nroot, euclidian_distance))