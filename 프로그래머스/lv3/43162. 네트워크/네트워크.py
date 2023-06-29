from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    while sum(visited) < n:
        done = True
        for i, v in enumerate(visited):
            if not v:
                break
        q = deque([i])
        while len(q) > 0:
            i = q.popleft()
            for j, c in enumerate(computers[i]):
                if (not visited[j]) and (c == 1):
                    visited[j] = True
                    q.append(j)
        answer += 1
    return answer