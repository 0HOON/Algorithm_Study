from copy import deepcopy as dc
from queue import PriorityQueue

def FindEasyPath(summit, memo, nodes, gates, min_d):
    #nodes = dc(nodes)
    dist = [float('inf')]*len(nodes)
    visited = [False]*len(nodes)
    dist[summit] = 0
    q = PriorityQueue()
    
    for k, w in memo[summit].items():
        q.put((w, k))
        dist[k] = w
    
    not_visited = len(gates)
    
    while not_visited > 0 and not q.empty():
        d, k = q.get()
        if visited[k] or (d > dist[k]):
            continue
        visited[k] = True
        if nodes[k] == 1:
            not_visited -= 1
            
        if nodes[k] == 0: #쉼터가 아니면 중지.
            for n, w in memo[k].items(): # 인접 노드
                if (not visited[n]):
                    w = max(w, dist[k])
                    if (dist[n] > w and min_d > w):
                        q.put((w, n))
                        dist[n] = w
    
    min_int = float('inf')
    for g in gates:
        if min_int > dist[g]:
            min_int = dist[g]
    
    return min_int
    
def solution(n, paths, gates, summits):
    memo = {}
    nodes = [0] * (n+1) # 0: 쉼터. 1: 입구 2: 봉우리
    for i in gates:
        nodes[i] = 1
    for i in summits:
        nodes[i] = 2
        
    for a, b, w in paths:
        if memo.get(a) == None:
            memo[a] = {b: w}
        else:
            memo[a][b] = w
        if memo.get(b) == None:
            memo[b] = {a: w}
        else:    
            memo[b][a] = w
    
    min_int = float('inf')
    min_s = 0
    for s in sorted(summits):
        tmp = FindEasyPath(s, memo, nodes, gates, min_int)
        if tmp < min_int:
            min_s = s
            min_int = tmp
    answer = [min_s, min_int]
    
    
    return answer