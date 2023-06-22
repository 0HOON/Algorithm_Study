import sys
sys.setrecursionlimit(1000000)

def n_hop(n, memo):
    if n <= 1:
        return 1
    if memo[n] == -1:
        memo[n] = (n_hop(n-1, memo)+n_hop(n-2, memo))%1234567
        
    return memo[n]

def solution(n):
    memo = [-1] * 2001
    answer = n_hop(n, memo)
    return answer