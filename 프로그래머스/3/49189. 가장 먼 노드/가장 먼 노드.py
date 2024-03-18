from collections import deque

def solution(n, edge):
    answer = 0
    edges = {}
    for a, b in edge:
        if edges.get(a):
            edges[a].append(b)
        else:
            edges[a] = [b]
        if edges.get(b):
            edges[b].append(a)
        else:
            edges[b] = [a]
            
    visited = [False]*(n+1)
    
    q = deque([(1, 0)])
    max_dist = 0
    while len(q) > 0:
        node, dist = q.popleft()
        
        if visited[node]:
            continue
            
        visited[node] = True
        
        for next_node in edges[node]:
            if not visited[next_node]:
                q.append((next_node, dist+1))
        
        if max_dist == dist:
            answer += 1
        elif dist > max_dist:
            max_dist = dist
            answer = 1
            
    return answer