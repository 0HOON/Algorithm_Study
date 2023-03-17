from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    max_len = 2*(len(queue1) + len(queue2))
    sum1 = sum(queue1)
    total = sum1 + sum(queue2)
    if total % 2 != 0:
        return -1
    half = total//2
    while sum1 != half:
        if sum1 > half:
            tmp = queue1.popleft()
            sum1 -= tmp
            queue2.append(tmp)
        else:
            tmp = queue2.popleft()
            sum1 += tmp
            queue1.append(tmp)
        answer += 1
        if answer > max_len:
            return -1
    return answer