from collections import deque

def possible_step(i, j, land):
    res = []
    if i > 0:
        res.append((i-1, j))
    if j > 0:
        res.append((i, j-1))
    if i < len(land)-1:
        res.append((i+1, j))
    if j < len(land[0])-1:
        res.append((i, j+1))
    return res
    
def travel(i, j, n, land, count_map):
    q = deque([(i, j)])
    total = [0, n]
    while len(q) > 0:
        r, c = q.popleft()
        if type(count_map[r][c]) == list:
            continue
        count_map[r][c] = total
        total[0] += 1
        for rr, cc in possible_step(r, c, land):
            if land[rr][cc] and (type(count_map[rr][cc]) != list):
                q.append((rr, cc))
            
def solution(land):
    answer = 0
    count_map = [[0]*len(land[0]) for _ in range(len(land))]
    n = 0
    for j in range(len(land[0])):
        total = 0
        tmp = []
        for i in range(len(land)):
            if land[i][j]:
                if type(count_map[i][j]) != list:
                    n += 1
                    travel(i, j, n, land, count_map)
                    
                if (count_map[i][j][1] not in tmp):
                    total += count_map[i][j][0]
                    tmp.append(count_map[i][j][1])
                
        if total > answer:
            answer = total
    
    return answer