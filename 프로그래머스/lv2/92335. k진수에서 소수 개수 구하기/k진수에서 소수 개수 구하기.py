from math import sqrt

def ToK(n, k):
    # k진수(list)로 변환
    n_k = []
    while n > 0:
        q, r = divmod(n, k)
        n_k.append(r)
        n = q
    return n_k[::-1]

def IsPrime(n_k):
    # 소수인지 판별
    num = 0
    for i, n in enumerate(n_k[::-1]):
        num += n*(10**i)
        
    if num == 2:
        return True
    if num == 1 or num%2 == 0:
        return False
    
    i = 3
    while i <= sqrt(num):
        if num%i == 0:
            return False
        i += 2
    return True

def solution(n, k):
    answer = 0
    n_k = ToK(n, k)
    q = []
    for num in n_k:
        if num == 0:
            if len(q) > 0:
                answer += IsPrime(q)
                
                q = []
            else:
                continue
        else:
            q.append(num)
            
    if len(q) > 0:
        answer += IsPrime(q)
        
    return answer