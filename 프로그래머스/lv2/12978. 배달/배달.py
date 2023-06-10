def update(dist, memo, visited):
    min_vil = 0
    min_d = 5000000
    for i, d in enumerate(dist):
        if d <= min_d and not(visited[i]):
            min_d = d
            min_vil = i
            
    visited[min_vil] = True
    for i, d in enumerate(memo[min_vil]):
        if not(visited[i]) and d+min_d < dist[i]:
            dist[i] = d+min_d
    
def solution(N, road, K):
    memo = [[500000]*(N+1) for _ in range(N+1)]
    dist = [500000]*(N+1)
    for a, b, c in road:
        memo[a][b] = min(memo[a][b], c)
        memo[b][a] = min(memo[a][b], c)
        if a == 1:
            dist[b] = min(dist[b], c)
    
    visited = [False]*(N+1)
    dist[1] = 0
    
    for _ in range(N):
        update(dist, memo, visited)
        
    answer = 0
    for d in dist:
        answer += d<=K
        
    return answer