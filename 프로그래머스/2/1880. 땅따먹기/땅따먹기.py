import sys

sys.setrecursionlimit(1000000)

def max_sum(i, j, land, memo):
    if memo[i][j] > -1:
        return memo[i][j]
    if i == 0:
        memo[i][j] = land[i][j]
        return memo[i][j]
    
    last_sums = []
    for col in range(4):
        s = max_sum(i-1, col, land, memo)
        last_sums.append(s)
    
    for col, p in enumerate(land[i]):
        tmp = [n for idx, n in enumerate(last_sums) if idx != col]
        memo[i][col] = max(tmp) + p
        
    return memo[i][j]

def solution(land):
    answer = 0
    memo = [[-1]*4 for _ in range(len(land))]
    
    s = max_sum(len(land)-1, 0, land, memo)
    
    answer = max(memo[-1])
    
    return answer