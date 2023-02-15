import sys
n = sys.stdin.readline()
n = int(n)

edges = {(i+1): [] for i in range(n)}

for i in range(n-1):
    a, b = list(map(int, sys.stdin.readline().split()))
    edges[a].append(b)
    edges[b].append(a)

queue = [1]
visited = [-1] * n
while len(queue) > 0:
    q = queue.pop(0)
    for node in edges[q]:
        if visited[node-1] < 0:
            queue.append(node)
            visited[node-1] = q

for p in visited[1:]:
    print(p)