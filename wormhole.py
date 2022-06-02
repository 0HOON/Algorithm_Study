# 1865 웜홀 골드3

inf = 99999

def BF(N, edges):
    d = {i:inf for i in range(N)}
    d[0] = 0
    for _ in range(N-1):
        for es in edges:
            for ee in edges[es]:
                d[ee] = min(d[es] + edges[es][ee], d[ee]) 

    for es in edges:
        for ee in edges[es]:
            if d[es] + edges[es][ee] < d[ee]:
                return True
    return False

TC = int(input())
result = []
for tc in range(TC):
    N, M, W = list(map(int, input().split()))

    edges = {v:{} for v in range(N)}
    
    for m in range(M):
        S, E, T = list(map(int, input().split()))
        edges[S-1][E-1] = min(edges[S-1].get(E-1, 10000), T)
        edges[E-1][S-1] = min(edges[E-1].get(S-1, 10000), T)

    for w in range(W):
        S, E, T = list(map(int, input().split()))
        edges[S-1][E-1] = min(edges[S-1].get(E-1, 10000), -T)

    result.append(BF(N, edges))

for r in result:
    if r:
        print("YES")
    else:
        print("NO")