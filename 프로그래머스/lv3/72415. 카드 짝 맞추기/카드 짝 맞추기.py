from copy import deepcopy
from itertools import permutations

def check(board, r, c, d):
    n_0 = 0
    if r > 0:
        if d[r-1][c] == -1:
            d[r-1][c] = d[r][c] + 1
            n_0 += 1
        for row in range(r-1, -1, -1):
            if board[row][c] > 0 or row==0:
                if d[row][c] == -1:
                    n_0 += 1
                    d[row][c] = d[r][c] + 1
                break
    if r < 3:
        if d[r+1][c] == -1:
            d[r+1][c] = d[r][c] + 1
            n_0 += 1
        for row in range(r+1, 4):
            if board[row][c] > 0 or row==3:
                if d[row][c] == -1:
                    n_0 += 1
                    d[row][c] = d[r][c] + 1
                break
    if c > 0:
        if d[r][c-1] == -1:
            d[r][c-1] = d[r][c] + 1
            n_0 += 1
        for col in range(c-1, -1, -1):
            if board[r][col] > 0 or col==0:
                if d[r][col] == -1:
                    n_0 += 1
                    d[r][col] = d[r][c] + 1
                break
    if c < 3:
        if d[r][c+1] == -1:
            d[r][c+1] = d[r][c] + 1
            n_0 += 1
        for col in range(c+1, 4):
            if board[r][col] > 0 or col==3:
                if d[r][col] == -1:
                    n_0 += 1
                    d[r][col] = d[r][c] + 1
                break
    return n_0

def get_d(board, r, c):
    d = [[-1]*4 for _ in range(4)]
    d[r][c] = 0
    n_0 = 15
    ii = 0
    while n_0 > 0:
        old_d = deepcopy(d)
        for i in range(4):
            for j in range(4):
                if old_d[i][j] == ii:
                    n_0 -= check(board, i, j, d)
        ii += 1
                    
    return d
                        
def find_next(board, d):
    min_d = 100
    min_n = 0
    for i in range(4):
        for j in range(4):
            if d[i][j] < min_d and board[i][j] > 0:
                min_d = d[i][j]
                min_rc = (i, j)
                min_n = board[i][j]
                
    return min_n, min_rc

def find_n(board, n):
    rc = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == n:
                rc.append((i, j))
    return rc
            
def solution(board, r, c):
    total_n = 0
    card_list = []
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0 and board[i][j] not in card_list:
                card_list.append(board[i][j])
    
    min_d = 10000
    r_ori = r
    c_ori = c
    for card_order in permutations(card_list, len(card_list)):
        b = deepcopy(board)
        total = 0
        r = r_ori
        c = c_ori
        for n in card_order:
            d = get_d(b, r, c)
            rc = find_n(b, n)
            
            tmp_b = deepcopy(b)
            tmp_b[rc[0][0]][rc[0][1]] = 0
            d1 = d[rc[0][0]][rc[0][1]] + get_d(tmp_b, rc[0][0], rc[0][1])[rc[1][0]][rc[1][1]]
            tmp_b = deepcopy(b)
            tmp_b[rc[1][0]][rc[1][1]] = 0
            d2 = d[rc[1][0]][rc[1][1]] + get_d(tmp_b, rc[1][0], rc[1][1])[rc[0][0]][rc[0][1]]
            if d1 < d2:
                total += d1
                b[rc[0][0]][rc[0][1]] = 0
                b[rc[1][0]][rc[1][1]] = 0
                r = rc[1][0]
                c = rc[1][1]
            else:
                total += d2
                b[rc[0][0]][rc[0][1]] = 0
                b[rc[1][0]][rc[1][1]] = 0
                r = rc[0][0]
                c = rc[0][1]
        if total < min_d:
            min_d = total
    answer = min_d + len(card_list)*2
    
    return answer