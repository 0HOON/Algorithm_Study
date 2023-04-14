from math import sqrt, ceil, floor
def solution(r1, r2):
    answer = 0
    for x in range(1, r1):
        y1 = ceil(sqrt(r1**2 - x**2))
        y2 = floor(sqrt(r2**2 - x**2))
        answer += (y2-y1+1)*4
    for x in range(r1, r2):
        answer += (floor(sqrt(r2**2 - x**2)))*4
    answer += (r2-r1+1)*4
    
    return answer