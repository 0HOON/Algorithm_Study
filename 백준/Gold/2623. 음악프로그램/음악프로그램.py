N, M = list(map(int, input().split()))
memo = {i:[] for i in range(N)}
prev = [0 for _ in range(N)]

for i in range(M):
  tmp = list(map(int, input().split()))[1:]
  for j, t in enumerate(tmp):
    memo[t-1].extend(tmp[j:])
    prev[t-1] += j

visited = [False] * N

changed = True
ans = []
while changed:
  changed = False
  for i, p in enumerate(prev):
    if not visited[i] and p == 0:
      ans.append(i+1)
      visited[i] = True
      for j in memo[i]:
        prev[j-1] -= 1
      changed = True
      break

if sum(visited) < N:
  print(0)
else:
  for a in ans:
    print(a)