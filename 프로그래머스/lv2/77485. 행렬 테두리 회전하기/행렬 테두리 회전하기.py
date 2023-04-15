from collections import deque
from copy import deepcopy

def move(board, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    tmp = []
    
    for y in range(y1, y2+1):
        tmp.append((x1, y))
    for x in range(x1+1, x2+1):
        tmp.append((x, y))
    for y in range(y2-1, y1-1, -1):
        tmp.append((x, y))
    for x in range(x2-1, x1, -1):
        tmp.append((x, y))
    
    tmp = list(reversed(tmp))
    tmp_ = deque(tmp)
    tmp_.rotate(1)
    #result = deepcopy(board)
    min_n = board[x1][y1]
    origin = board[x1][y1]
    for (bx, by), (ax, ay) in zip(tmp, tmp_):
        board[ax][ay] = board[bx][by]
        if min_n > board[ax][ay]:
            min_n = board[ax][ay]
    board[x1][y1+1] = origin
    return min_n

def solution(rows, columns, queries):
    answer = []
    board = [[(i+1) + (columns*j) for i in range(columns)] for j in range(rows)]
    for x1, y1, x2, y2 in queries:
        ans = move(board, x1, y1, x2, y2)
        answer.append(ans)
    return answer