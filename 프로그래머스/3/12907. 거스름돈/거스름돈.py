def solution(n, money):
    money = sorted(money)
    memo = [0]*(n+1)
    
    memo[0] = 1
    
    for m in money:
        for i in range(n+1):
            if i-m >= 0:
                memo[i] += memo[i-m]
    return memo[-1]