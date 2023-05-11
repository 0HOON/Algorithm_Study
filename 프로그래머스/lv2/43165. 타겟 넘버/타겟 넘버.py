from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(numbers[0], 0), (-numbers[0], 0)])
    while len(q) > 0:
        n, i = q.popleft()
        if i == len(numbers)-1:
            answer += n==target
        else:
            q.append((n+numbers[i+1], i+1))
            q.append((n-numbers[i+1], i+1))
    return answer