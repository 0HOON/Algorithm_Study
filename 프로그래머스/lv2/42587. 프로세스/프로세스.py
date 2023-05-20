from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    max_p = max(q)
    done = False
    n = 1
    while not done:
        p = q.popleft()
        location -= 1
        if p == max_p:
            if location == -1:
                return n
            max_p = max(q)
            n += 1
        else:
            q.append(p)
            if location == -1:
                location = len(q)-1
    return answer