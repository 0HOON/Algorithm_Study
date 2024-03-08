

def solution(n, k):
    answer = []
    factorials = [1]
    tmp = 1
    while tmp <= n:
        factorials.append(factorials[tmp-1]*tmp)
        tmp += 1
    
    remaining = [i for i in range(1, n+1)]
    idx = 1
    while k > 0:
        ans, k = divmod(k, factorials[n-idx])
        #print(n-idx, factorials[n-idx], ans, k, answer)
        if k == 0:
            answer.append(remaining.pop(ans-1))
            answer.extend(reversed(remaining))
        else:
            answer.append(remaining.pop(ans))  
        idx += 1
        #print(answer, remaining)
    return answer