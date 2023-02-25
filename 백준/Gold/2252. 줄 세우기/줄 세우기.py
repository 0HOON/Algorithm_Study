N, M = list(map(int, input().split()))

memo = {i:[] for i in range(1, N+1)}
prev = [0] * (N+1)
for _ in range(M):
  a, b = list(map(int, input().split()))
  memo[a].append(b)
  prev[b] += 1

q = []
visited = [False] * (N+1)
while sum(prev) > 0 or sum(visited) < N:
  for i in range(1, N+1):
    if (not visited[i]) and prev[i] == 0:
      q.append(i)
      visited[i] = True
      for j in memo[i]:
        prev[j] -= 1
      continue
      
print(' '.join(map(str, q)))