def MM(s, e, matrices, memo):
  if s == e:
    return 0
  if memo[s][e] != -1:
    return memo[s][e]
  
  min_ = float('inf')
  for i in range(s, e):
    tmp = (
      MM(s, i, matrices, memo) 
      + MM(i+1, e, matrices, memo) 
      + matrices[s][0]*matrices[i][1]*matrices[e][1]
      )
    if tmp < min_:
      min_ = tmp
  
  memo[s][e] = min_
  return memo[s][e]


N = int(input())
matrices = []
memo = [[-1]*N for _ in range(N)]
for i in range(N):
  matrices.append(list(map(int, input().split())))

print(MM(0, N-1, matrices, memo))