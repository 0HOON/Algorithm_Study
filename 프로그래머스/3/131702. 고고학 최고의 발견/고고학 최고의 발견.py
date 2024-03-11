from copy import deepcopy
from itertools import product

def tictoc(clockhands, i, j, n):
    if n == 0:
        return
    sz = len(clockhands)
    if i > 0:
        clockhands[i-1][j] = (clockhands[i-1][j] + n)%4
    if i < sz-1:
        clockhands[i+1][j] = (clockhands[i+1][j] + n)%4
    if j > 0:
        clockhands[i][j-1] = (clockhands[i][j-1] + n)%4
    if j < sz-1:
        clockhands[i][j+1] = (clockhands[i][j+1] + n)%4
    
    clockhands[i][j] = (clockhands[i][j] + n)%4

def check(clockhands):
    s = 0
    for row in clockhands:
        s += sum(row)
        
    return s == 0

def _solve(clockhands):
    n_total = 0
    for i, row in enumerate(clockhands[:-1]):
        for j, c in enumerate(row):
            n = (4-c)%4
            tictoc(clockhands, i+1, j, n)
            n_total += n
    
    return check(clockhands), n_total

def solution(clockHands):
    answer = 99999999999
    for ns in product((0, 1, 2, 3), repeat=len(clockHands)):
        tmp = deepcopy(clockHands)
        total_n = 0
        for i, n in enumerate(ns):
            tictoc(tmp, 0, i, n)
            total_n += n
            
        done, n = _solve(tmp)
        total_n += n
        
        if done and answer > total_n:
            answer = total_n
        
    return answer