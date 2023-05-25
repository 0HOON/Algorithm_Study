def solution(n):
    answer = 0
    cumsum = [0]
    for i in range(n):
        cumsum.append(cumsum[-1]+i+1)
        
    i = 0
    j = 1
    while i < j:
        s = cumsum[j] - cumsum[i]
        if s < n:
            j += 1
            if j >= len(cumsum):
                j = len(cumsum)-1
                
        elif s > n:
            i += 1
            
        elif s == n:
            answer += 1
            i += 1
    return answer