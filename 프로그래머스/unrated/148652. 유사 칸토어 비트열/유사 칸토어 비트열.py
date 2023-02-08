# 5진수로 나타내고 변환 가능.

def check(num):
    while num > 0:
        num, mod = divmod(num, 5)
        if mod == 2:
            return 0
    return 1
    
    
def solution(n, l, r):
    answer = 0
    for x in range(l-1, r):
        answer += check(x)
    return answer