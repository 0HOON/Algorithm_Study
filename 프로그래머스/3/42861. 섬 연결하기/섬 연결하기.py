from heapq import heappush, heappop
def solution(n, costs):
    answer = 0
    neighbors = {i:[] for i in range(n)}
    for a, b, c in costs:
        neighbors[a].append((b, c))
        neighbors[b].append((a, c))
        
    visited = [0]*n
    q = [(0, 0)]
    while len(q) > 0:
        cost, i = heappop(q)
        if visited[i]:
            continue
        visited[i] = True
        answer += cost
        for n, c in neighbors[i]:
            if not visited[n]:
                heappush(q, (c, n))
    return answer