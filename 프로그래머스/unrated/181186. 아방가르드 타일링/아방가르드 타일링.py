import sys
sys.setrecursionlimit(1000000)


def dp(n, memo, cumsum):
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = (dp(n-3, memo, cumsum) * 5 + dp(n-2, memo, cumsum) * 2 + dp(n-1, memo, cumsum)) % 1000000007
    memo[n] += cumsum[3][n-4] * 2
    memo[n] += cumsum[n%3][n-4] * 2
        
    memo[n] = memo[n] % 1000000007
    cumsum[3][n] = (cumsum[3][n-1] + memo[n]) % 1000000007
    cumsum[n%3][n] = (cumsum[n%3][n-1] + memo[n]) % 1000000007
    cumsum[(n+1)%3][n] = cumsum[(n+1)%3][n-1]
    cumsum[(n+2)%3][n] = cumsum[(n+2)%3][n-1]
    return memo[n]

def solution(n):
    answer = 0
    memo = [-1] * (n+1)
    memo[0] = 1
    memo[1] = 1
    cumsum = [[0] * (n+1) for _ in range(4)] # 나머지 0, 1, 2, 전체
    cumsum[3][0] = 1
    cumsum[0][0] = 1
    
    cumsum[3][1] = 2
    cumsum[0][1] = 1
    cumsum[1][1] = 1
    if n >= 2:
        memo[2] = 3
        cumsum[3][2] = 5
        cumsum[0][2] = 1
        cumsum[1][2] = 1
        cumsum[2][2] = 3
    if n >= 3:
        memo[3] = 10
        cumsum[3][3] = 15
        cumsum[0][3] = 11
        cumsum[1][3] = 1
        cumsum[2][3] = 3
    answer = dp(n, memo, cumsum)
    return answer