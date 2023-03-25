def Find(p, n):
  tmp = [n]
  while p[n] != n:
    tmp.append(p[n])
    n = p[n]
  
  for i in tmp:
    p[i] = n
  return n
  
N, M = list(map(int, input().split()))
roads = []
for i in range(M):
  roads.append(list(map(int, input().split())))

roads = sorted(roads, key=lambda x: x[2])
parents = [i for i in range(N+1)]
n = 0
ans = 0
for a, b, w in roads:
  if n == N-2:
    break
  g_a = Find(parents, a)
  g_b = Find(parents, b)
  if g_a != g_b:
    parents[g_b] = g_a
    ans += w
    n += 1
  
print(ans)