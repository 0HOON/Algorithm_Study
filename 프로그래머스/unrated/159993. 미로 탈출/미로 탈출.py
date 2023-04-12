from collections import deque

def possible_move(maps, i, j):
    res = []
    if i > 0:
        res.append((i-1, j))
    if i < len(maps)-1:
        res.append((i+1, j))
    if j > 0:
        res.append((i, j-1))
    if j < len(maps[0])-1:
        res.append((i, j+1))
    
    return res

def solution(maps):
    answer = 0
    R = len(maps)
    C = len(maps[0])
    maps = [list(r) for r in maps]
    
    for r, row in enumerate(maps):
        if 'S' in row:
            c = row.index('S')
            row[c] = 'O'
            break
    
    success = False
    visited = [[False]*C for _ in range(R)]
    q = deque([(r, c, 0)])
    while len(q) > 0:
        r, c, n = q.popleft()
        if maps[r][c] == 'L':
            answer += n
            success = True
            break
        if visited[r][c] or maps[r][c] == 'X':
            continue
        visited[r][c] = True
        pm = possible_move(maps, r, c)
        for rr, cc in pm:
            if not visited[rr][cc]:
                q.append((rr, cc, n+1))
    
    if not success:
        return -1
    
    success = False
    visited = [[False]*C for _ in range(R)]
    q = deque([(r, c, 0)])
    while len(q) > 0:
        r, c, n = q.popleft()
        if maps[r][c] == 'E':
            answer += n
            success = True
            break
        if visited[r][c] or maps[r][c] == 'X':
            continue
        visited[r][c] = True
        pm = possible_move(maps, r, c)
        for rr, cc in pm:
            if not visited[rr][cc]:
                q.append((rr, cc, n+1))
                
    if not success:
        return -1
    
    return answer