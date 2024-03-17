import heapq

def get_dist(s, dist):
    new_dist = [1e7]*(len(dist))
    q = [(0, s)]
    while len(q) > 0:
        d, destination = heapq.heappop(q)
        if new_dist[destination] > d: # 아직 방문 안했다면
            new_dist[destination] = d
            for i, dd in enumerate(new_dist):
                if dd == 1e7 and dist[destination][i] < 1e7: # 방문 안한곳들
                    heapq.heappush(q, (d+dist[destination][i], i))
    return new_dist
    

def solution(n, s, a, b, fares):
    answer = 0
    dist = [[1e7]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
        
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
        
    dist_s = get_dist(s, dist)
    min_fare = 1e7
    
    for i in range(n+1):
        dist_i = get_dist(i, dist)
        fare = dist_i[a] + dist_i[b] + dist_s[i]
        if min_fare > fare:
            min_fare = fare
    
    return min_fare