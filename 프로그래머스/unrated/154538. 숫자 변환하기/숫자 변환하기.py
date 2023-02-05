from collections import deque

def check(queue, checked, x, y, n_op):
    if x < y and not checked[x]:
        queue.append((x, n_op+1))
        checked[x] = True
        return False
    elif x == y:
        return True

def solution(x, y, n):
    if x == y:
        return 0
    
    answer = -1
    queue = deque([(x, 0)])
    checked = [False]*1000000
    while len(queue) > 0:
        tmp, n_op = queue.popleft()
        a = tmp * 3
        b = tmp * 2
        c = tmp + n
        if check(queue, checked, a, y, n_op):
            return n_op + 1
        if check(queue, checked, b, y, n_op):
            return n_op + 1
        if check(queue, checked, c, y, n_op):
            return n_op + 1
        
    return answer