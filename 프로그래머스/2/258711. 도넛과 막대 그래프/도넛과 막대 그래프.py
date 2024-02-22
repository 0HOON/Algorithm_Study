from collections import deque
    
def solution(edges):
    graph = {}
    # 그래프 생성
    # 들어오는 edge 없고 나가는 edge 2개 이상이면 생성된 정점
    # 나가는 edge 없는 node 있으면 막대
    # 나가는 edge 2개인 node 있으면 8자
    # 아니면 도넛
    edge_out = [0] * 1000001
    edge_in = [0] * 1000001
    graph = [[] for _ in range(1000001)]
    all_nodes = []
    
    for a, b in edges:
        all_nodes.extend([a, b])
        graph[a].append(b)
            
        edge_out[a] += 1
        edge_in[b] += 1
                
    answer = [0, 0, 0, 0]
    
    all_nodes = tuple(set(all_nodes))
    
    for node in all_nodes:
        if edge_out[node] - edge_in[node] > 1:
            answer[0] = node
        elif edge_out[node] > 1:
            answer[3] += 1
        elif edge_out[node] == 0:
            answer[2] += 1
    
    answer[1] = edge_out[answer[0]] - answer[2] - answer[3]
        
    return answer