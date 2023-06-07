from copy import deepcopy
def get_d(board, r, c):
    d = [[-1]*4 for _ in range(4)]
    d[r][c] = 100
    n_0 = 15
    for row in range(r-1, -1, -1):
        d[row][c] = 1
        n_0 -= 1
        if board[row][c] > 0:
            break
    for row in range(r+1, 4):
        d[row][c] = 1
        n_0 -= 1
        if board[row][c] > 0:
            break
    for col in range(c-1, -1, -1):
        d[r][col] = 1
        n_0 -= 1
        if board[r][col] > 0:
            break
    for col in range(c+1, 4):
        d[r][col] = 1
        n_0 -= 1
        if board[r][col] > 0:
            break
    while n_0 > 0:
        old_d = deepcopy(d)
        for i in range(4):
            for j in range(4):
                if old_d[i][j] > 0:
                    if i > 0 and d[i-1][j] == -1:
                        d[i-1][j] = old_d[i][j]+1
                        n_0 -= 1
                    if i < 3 and d[i+1][j] == -1:
                        d[i+1][j] = old_d[i][j]+1
                        n_0 -= 1
                    if j > 0 and d[i][j-1] == -1:
                        d[i][j-1] = old_d[i][j]+1
                        n_0 -= 1
                    if j < 3 and d[i][j+1] == -1:
                        d[i][j+1] = old_d[i][j]+1
                        n_0 -= 1
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
    for i in range(4):
        for j in range(4):
            if board[i][j] == n:
                return i, j
            
def solution(board, r, c):
    total_n = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                total_n += 1
    
    answer = total_n
    to_find = 0
    
    while total_n > 0:
        
        d = get_d(board, r, c)
        if board[r][c] > 0:
            to_find = board[r][c]
            board[r][c] = 0
            total_n -= 1
            for b in board:
                print(b)
            print(r, c, answer)
        else:
            to_find, rc = find_next(board, d)
            answer += d[rc[0]][rc[1]]
            total_n -= 1
            
            r = rc[0]
            c = rc[1]
            board[r][c] = 0
            d = get_d(board, r, c)
            for b in board:
                print(b)
            print(r, c, answer)
        r, c = find_n(board, to_find)
        answer += d[r][c]
        board[r][c] = 0
        total_n -= 1
        to_find = 0
        for b in board:
            print(b)
        print(r, c, answer)
    return answer