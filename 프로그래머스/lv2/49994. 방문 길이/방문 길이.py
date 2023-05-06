from copy import deepcopy

def move(loc, d, memo):
    loc_now = deepcopy(loc)
    if d == 'U':
        loc[1] += 1
    elif d == 'D':
        loc[1] -= 1
    elif d == 'L':
        loc[0] -= 1
    elif d == 'R':
        loc[0] += 1
    
    if loc[1] > 5:
        loc[1] = 5
        return 0
    elif loc[1] < -5:
        loc[1] = -5
        return 0
    elif loc[0] > 5:
        loc[0] = 5
        return 0
    elif loc[0] < -5:
        loc[0] = -5
        return 0
    if (memo.get((loc[0], loc[1], loc_now[0], loc_now[1]), False) or 
        memo.get((loc_now[0], loc_now[1], loc[0], loc[1]), False)):
        return 0
    
    memo[(loc[0], loc[1], loc_now[0], loc_now[1])] = True
    memo[(loc_now[0], loc_now[1], loc[0], loc[1])] = True
    return 1

def solution(dirs):
    answer = 0
    loc = [0, 0]
    memo = {}
    for d in dirs:
        answer += move(loc, d, memo)
    return answer