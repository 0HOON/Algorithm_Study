from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    q = deque([])
    n = 0
    for i, p in enumerate(prices):
        if len(q) <= 0  or p >= q[-1][1]:
            q.append((i, p))
        else:
            while True:
                if len(q) <= 0  or p >= q[-1][1]:
                    break
                else:
                    ii, pp = q.pop()
                    answer[ii] = n-ii
            q.append((i, p))
        n += 1
        
    while len(q) > 0:
        ii, pp = q.pop()
        answer[ii] = n-ii-1
        
    return answer