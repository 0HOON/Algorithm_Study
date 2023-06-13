def solution(n, roads, sources, destination):
    answer = []
    memo = {i:[] for i in range(n+1)}
    for a,b in roads:
        memo[a].append(b)
        memo[b].append(a)
    
    dist = [-1]*(n+1)
    dist[destination]=0
    next_list = [destination]
    visited = [False]*(n+1)
    done = len(next_list) == 0
    while not done:
        tmp = []
        for next_node in next_list:
            visited[next_node] = True
            for i in memo[next_node]:
                if dist[i] == -1:
                    dist[i] = dist[next_node] + 1
                    tmp.append(i)
        next_list = tmp        
        done = len(next_list) == 0
    answer = [dist[i] for i in sources]
    return answer