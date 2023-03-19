def solution(want, number, discount):
    answer = 0
    memo = {w: n for w, n in zip(want, number)}
    total = 0 
    for i, item in enumerate(discount):
        if i > 9:
            it = discount[i-10]
            if memo.get(it) != None:
                memo[it] += 1
                if memo[it] > 0:
                    total -= 1
            
        if memo.get(item) != None:
            memo[item] -= 1
            if memo[item] >= 0:
                total += 1
        
        if total == 10:
            answer += 1
        
        
    return answer