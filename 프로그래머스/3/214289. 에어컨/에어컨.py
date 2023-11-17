import sys
sys.setrecursionlimit(1000000)

def up_cost(temp, temperature, a):
    if temp <= temperature:
        return 0
    else:
        return a

def down_cost(temp, temperature, a):
    if temp >= temperature:
        return 0
    else:
        return a

def is_ok(temp, t1, t2):
    return (temp <= t2) and (temp >= t1)

def solve(t, temp, memo, temperature, t1, t2, a, b, onboard):
    if memo[t][temp] != -1:
        return memo[t][temp]
    
    if onboard[t] and not is_ok(temp, t1, t2):
        memo[t][temp] = 1000000
        return memo[t][temp]
    
    min_cost = solve(t-1, temp, memo, temperature, t1, t2, a, b, onboard) + (0 if temp == temperature else b)
    
    if temp > 0:
        min_cost = min(min_cost, solve(t-1, temp-1, memo, temperature, t1, t2, a, b, onboard) + up_cost(temp, temperature, a))
    
    if temp < 50:
        min_cost = min(min_cost, solve(t-1, temp+1, memo, temperature, t1, t2, a, b, onboard) + down_cost(temp, temperature, a))
    
    memo[t][temp] = min_cost
    return memo[t][temp]

def solution(temperature, t1, t2, a, b, onboard):
    answer = 99999999999
    temperature += 10
    t1 += 10
    t2 += 10
    
    if onboard[-1] == 0:
        for i in range(1, len(onboard)):
            if onboard[-i] == 1:
                onboard = onboard[:-i+1]
                break
                
    memo = [[-1] * (51) for _ in range(len(onboard))]
    for t in range(51):
        if t == temperature:
            memo[0][t] = 0
        else:
            memo[0][t] = 1000000
        
    for temp in range(t1, t2+1):
        answer = min(answer, solve(len(onboard)-1, temp, memo, temperature, t1, t2, a, b, onboard))
    
    return answer