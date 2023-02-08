from math import sqrt, floor
def find_n(n):
    ans = 0 
    for i in range(1, floor(sqrt(n))+1):
        if i*i == n:
            ans += 1
        elif n % i == 0:
            ans += 2
    return ans

def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        tmp_n = find_n(n)
        if tmp_n > limit:
            answer += power
        else: answer += tmp_n
        
    return answer