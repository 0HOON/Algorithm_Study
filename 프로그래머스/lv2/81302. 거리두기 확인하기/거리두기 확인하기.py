# direction: u, d, l, r
def PossibleIndices(i, j):
    idx = []
    if i > 0:
        idx.append((i-1, j, 0))
    if i < 4:
        idx.append((i+1, j, 1))
    if j > 0:
        idx.append((i, j-1, 2))
    if j < 4:
        idx.append((i, j+1, 3))
        
    return idx

def CheckNext(places, i, j, direction):
    if direction == 0 and i > 0:
        if places[i-1][j] == 'P':
            return False
    elif direction == 1 and i < 4:
        if places[i+1][j] == 'P':
            return False
    elif direction == 2 and j > 0:
        if places[i][j-1] == 'P':
            return False
    elif direction == 3 and j < 4:
        if places[i][j+1] == 'P':
            return False
        
    return True
    
def CheckPartition(places, i, j, partition):
    idx = []
    if not(partition[0] and partition[2]):
        if i > 0 and j > 0:
            idx.append((i-1, j-1))
    if not(partition[0] and partition[3]):
        if i > 0 and j < 4:
            idx.append((i-1, j+1))
    if not(partition[1] and partition[2]):
        if i < 4 and j > 0:
            idx.append((i+1, j-1))
    if not(partition[1] and partition[3]):
        if i < 4 and j < 4:
            idx.append((i+1, j+1))
        
    for ii, jj in idx:
        if places[ii][jj] == 'P':
            return False
        
    return True
        
def Check(places, i, j):
    # i, j 에 사람. 
    possible_indices_1 = PossibleIndices(i, j)
    partition = [False]*4
    for ii, jj, direction in possible_indices_1:
        if places[ii][jj] == 'P':
            return False
        elif places[ii][jj] == 'X':
            partition[direction] = True
        else:
            if not CheckNext(places, ii, jj, direction):
                return False
            
    return CheckPartition(places, i, j, partition)
                    
def solution(places):
    answer = []
    for p in places:
        ans = 1
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P' and not Check(p, i, j):
                    ans = 0
                    break
            if ans == 0:
                break
                    
        answer.append(ans)
        
    return answer