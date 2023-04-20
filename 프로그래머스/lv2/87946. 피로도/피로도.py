from collections import deque

def solution(k, dungeons):
    visited = 0    
    q = deque([(0, 0, k)]) # visited, 탐험한 던전 수, 남은 피로도
    answer = 0
    while len(q) > 0:
        visited, n, k = q.popleft()
        n_appended = 0
        for i in range(len(dungeons)):
            if (not (visited >> i) & 1) and dungeons[i][0] <= k:
                q.append((visited|(1<<i), n+1, k-dungeons[i][1]))
                n_appended += 1
                
        if n_appended == 0:
            answer = max(answer, n)
    return answer