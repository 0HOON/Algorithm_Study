def map2matrix(maps):
    return [[0 if c == 'X' else int(c) for c in row] for row in maps]
    
def check_island(map):
    island = [[0] * len(map[0]) for _ in range(len(map))]
    n = 0
    same = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] > 0:
                up = False
                left = False
                
                if i > 0 and island[i-1][j] > 0:
                    up = True
                if j > 0 and island[i][j-1] > 0:
                    left = True

                if (not up) and (not left):
                    n += 1
                    island[i][j] = n
                    same.append([n])
                elif up and (not left):
                    island[i][j] = island[i-1][j]
                elif (not up) and left:
                    island[i][j] = island[i][j-1]
                elif up and left:
                    island[i][j] = island[i][j-1]
                    a = island[i-1][j]
                    b = island[i][j-1]
                    if a != b:
                        aa = -1
                        bb = -1
                        for ii, group in enumerate(same):
                            if a in group:
                                aa = ii
                            if b in group:
                                bb = ii
                                
                        if aa != bb:
                            same[aa].extend(same[bb].copy())
                            del same[bb]
                            
    if len(same) < n:
        for i in range(len(map)):
            for j in range(len(map[0])):
                if island[i][j] > 0:
                    for k, group in enumerate(same):
                        if island[i][j] in group:
                            island[i][j] = k+1
                            break
        n = len(same)

    return island, n

def solution(maps):
    map = map2matrix(maps)
    c = 0
    for row in map:
        c += sum(row)
    if c == 0:
        return [-1]
    
    island, n = check_island(map)
    answer = [0] * n
    print(island, n)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if island[i][j] > 0:
                answer[island[i][j]-1] += map[i][j]
    
    return sorted(answer)