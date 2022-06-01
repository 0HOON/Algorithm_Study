# 1753 최단경로 골드5
# Dijkstra Algorithm

from cmath import inf


def d_search(f):
  if mm[f] != None:
    for i in mm[f]:
      t = i[0]
      if visited[t]:
        continue

      dd = d[f] + i[1]
      if dd < d[t]:
        d[t] = dd
        
  visited[f] = True


V, E = list(map(int, input().split()))
s = int(input()) - 1

mm = [None] * V
d = [inf] * V
d[s] = 0
visited = [False] * V

for i in range(E):
  u, v, w = list(map(int, input().split()))
  if mm[u-1] == None:
    mm[u-1] = [(v-1, w)]
    continue
  mm[u-1].append((v-1, w))

node = s

while True:
  d_search(node)
  min_next = inf
  for i in range(V):
    if (not visited[i]) and d[i] < min_next:
      min_next = d[i]
      node = i
  if min_next == inf:
    break

for i in d:
  if i == inf:
    print("INF")
    continue
  print(i)