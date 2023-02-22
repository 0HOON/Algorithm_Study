# 지금까지 방문한 도시 + 지금 있는 도시가 같을 때, 나머지 도시 도는 최소 경로는 동일.
# visited, i

def TSP(visited, i, memo):
  if memo[visited].get(i, None) != None:
    return memo[visited][i]

  if visited == 2**N-1:
    if w[i][0] > 0:
      return w[i][0]
    else:
      return float('inf')

  min_w = float('inf')
  for j, w_ in enumerate(w[i]):
    if w_ != 0 and not (visited & 2**j):
      visited += 2**j
      tmp = TSP(visited, j, memo) + w_
      if tmp < min_w:
        min_w = tmp
      visited -= 2**j
  
  memo[visited][i] = min_w
  return memo[visited][i]

N = int(input())
w = []
for i in range(N):
  w.append(list(map(int, input().split())))

visited = 1
memo = {i: {} for i in range(2**(N))}

print(TSP(visited, 0, memo))

