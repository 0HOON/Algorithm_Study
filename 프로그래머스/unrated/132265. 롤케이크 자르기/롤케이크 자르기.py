def solution(topping):
    answer = 0
    a = {}
    b = {}
    
    for t in topping:
        b[t] = b.get(t, 0) + 1
    
    for t in topping:
        a[t] = a.get(t, 0) + 1
        
        if b[t] == 1:
            del b[t]
        else:
            b[t] -= 1
        
        if len(a) == len(b):
            answer += 1
    
    return answer