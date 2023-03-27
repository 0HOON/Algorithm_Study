def LD(r, c):
  return (c-r) + N - 1

def RD(r, c):
  c = N-c-1
  return (c-r) + N - 1

N = int(input())
board = []
for _ in range(N):
  board.append(list(map(int, input().split())))

LD_dict = {}
min_L = 1000000
max_L = -1

for i in range(N):
  for j in range(N):
    ld = LD(i, j)
    LD_dict[ld] = LD_dict.get(ld, []) + [(i, j)]
    if board[i][j] and (ld < min_L):
      min_L = ld
    if board[i][j] and (ld > max_L):
      max_L = ld
if min_L == 1000000:
  print(0)
else:
  visited_R = 0

  stack = []
  for i, j in LD_dict[min_L]:
    if board[i][j]:
      stack.append((min_L, 2**RD(i, j), 1))

  ans = 0
  while len(stack) > 0:
    L, visited_R, n = stack.pop(-1)
    if L == max_L:
      if n > ans:
        ans = n
      continue
    
    added = 0
    for i, j in LD_dict[L+1]:
      if board[i][j] and not (visited_R & 2**RD(i, j)):
        stack.append((L+1, visited_R + 2**RD(i, j), n+1))
        added +=1 
    
    if added == 0:
      stack.append((L+1, visited_R, n))
    
  print(ans)