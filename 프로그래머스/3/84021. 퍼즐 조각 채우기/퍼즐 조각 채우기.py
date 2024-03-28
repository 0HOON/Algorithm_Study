from collections import deque
from copy import deepcopy

def rotate_board(board):
    b = [[0]*len(board) for _ in range(len(board[0]))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            b[j][len(board[0])-1-i] = board[i][j]
            
    return b
    
def get_puzzle_piece(i, j, board):
    q = deque([(0, 0)])
    shape = []
    while len(q) > 0:
        delta_r, delta_c = q.popleft()
        r, c = i+delta_r, j+delta_c
        if board[r][c] == 0:
            continue
        shape.append((delta_r, delta_c))
        board[r][c] = 0
        
        if r+1 < len(board) and board[r+1][c]:
            q.append((delta_r+1, delta_c))
        if c+1 < len(board[r]) and board[r][c+1]:
            q.append((delta_r, delta_c+1))
        if r-1 >= 0 and board[r-1][c]:
            q.append((delta_r-1, delta_c))
        if c-1 >= 0 and board[r][c-1]:
            q.append((delta_r, delta_c-1))
    
    return shape

def get_all_pieces(table):
    puzzle_pieces = []
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j]:
                puzzle_pieces.append(get_puzzle_piece(i, j, table))
    return puzzle_pieces
    
def solution(game_board, table):
    answer = 0
    # get list of puzzle pieces
    puzzle_pieces = get_all_pieces(table)
        
    board = [[0]*len(game_board[0]) for _ in range(len(game_board))] 
    for i, row in enumerate(game_board):
        for j, val in enumerate(row):
            board[i][j] = 1 - val
    
    
    for _ in range(4):
        b = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if b[i][j]:
                    p = get_puzzle_piece(i, j, b)
                    if p in puzzle_pieces:
                        get_puzzle_piece(i, j, board)
                        answer += len(p)
                        puzzle_pieces.remove(p)
        board = rotate_board(board)
        
    return answer