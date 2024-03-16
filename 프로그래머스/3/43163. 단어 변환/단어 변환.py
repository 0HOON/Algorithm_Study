from collections import deque

def solution(begin, target, words):
    words.append(begin)
    q = deque([(begin, 0)])
    visited = {w:False for w in words}
    
    while len(q) > 0:
        w, n = q.popleft()
        
        if visited[w]:
            continue
            
        visited[w] = True
        
        if w == target:
            return n
        
        for ww in words:
            if visited[ww]:
                continue
                
            diff = 0
            for a, b in zip(w, ww):
                diff += a!=b
            if diff == 1:
                q.append((ww, n+1))
            
    return 0