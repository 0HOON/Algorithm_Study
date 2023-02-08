import math
def solution(k, d):
    answer = 0
    r = d / k
    for a in range(math.floor(r) + 1):
        answer += math.floor(math.sqrt(r**2 - a**2)) + 1
    return answer