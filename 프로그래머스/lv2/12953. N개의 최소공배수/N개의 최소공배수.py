from copy import deepcopy

def solution(arr):
       
    prime_count = [0] * 100
    prime_count[1] = 1
    
    for a in arr:
        i = 2
        tmp = [0] * 100
        while a > 1:
            if a % i == 0:
                a = a//i
                tmp[i] += 1
            else:
                i += 1
        for i, p in enumerate(tmp):
            if prime_count[i] < p:
                prime_count[i] = p
    
    answer = 1
    for i, p in enumerate(prime_count):
        if p > 0:
            answer *= i**p
            
    return answer