import copy

def move_line(line, direction):
    if direction == 'r' or direction == 'd':
        line = reversed(line)

    result = []
    stop_i = 0
    finished = -1            # -1: not finished, 0: failed, 1: successed
    for l in line:
        if l  == 'R' or l == 'B':
            if result[stop_i] == 'O':
                finished = l == 'R' and finished == -1
                result.append('.')
            else:    
                result.append('.')
                result[stop_i+1] = l
                stop_i += 1
                
        elif l == '#' or l == 'O':
            result.append(l)
            stop_i = len(result)-1
        else:
            result.append(l)
    
    if direction == 'r' or direction == 'd':
        result = list(reversed(result))

    return finished, result

def move(board, direction):
    b = copy.deepcopy(board)
    f = -1
    if direction == 'r' or direction == 'l':
        for i, row in enumerate(b):
            if 'R' in row or 'B' in row:
                finished, new_row = move_line(row, direction)
                f = max(f, finished)
                b[i] = new_row
    elif direction == 'u' or direction == 'd':
        for j in range(M):
            col = []
            for i in range(N):
                col.append(b[i][j])
            if 'R' in col or 'B' in col:
                finished, new_col = move_line(col, direction)
                f = max(f, finished)
                for i in range(N):
                    b[i][j] = new_col[i]
    else:
        print("ERROR: Wrong Direction")
    
    return f, b
            
N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(input()))
directions = ['l', 'r', 'u', 'd']
q = [(0, board)]
ans = -1
while len(q) > 0:
    n, b = q.pop(0)
    if n == 10:
        break
    
    for d in directions:
        finished, new_b = move(b, d)
        if finished == 1:
            ans = n+1
            break
        elif finished == 0:
            continue
        elif finished == -1:
            if b != new_b:
                q.append((n+1, new_b))
    if ans != -1:
        break
print(ans)