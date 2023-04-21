def f(x):
    if x == 0:
        return 1
    tmp = x
    p = 0
    while tmp > 0:
        if not(tmp & 1):
            break
        tmp = tmp >> 1
        p += 1
    
    if (1<<p) > x:
        return (x+1)+((x+1)>>1)-1
    else:
        return x + 1 if p == 0 else x + (1<<(p-1))
    
def solution(numbers):
    answer = [f(n) for n in numbers]
    return answer