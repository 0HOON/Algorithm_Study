def check(i, j, t, visited, keys, stack, ans):
  if t == '.':              # 빈 곳
    stack.append((i, j))    
    visited[i][j] = True
  elif t == '$':            # 문서
    stack.append((i, j))
    ans += 1
    visited[i][j] = True
  elif t.isalpha():         # 알파벳 (키 or 문)
    if t.islower():         # 키
      stack.append((i, j))
      keys[t] = True
      visited[i][j] = True
    else:                   # 문
      if keys.get(t.lower()):
        stack.append((i, j))    
        visited[i][j] = True
      else:                 # 잠긴 문
        doors.append((i, j, t))
  else:                     # 벽
    visited[i][j] = True

  return ans 

def explore(i, j, visited):
  tmp = []
  if i > 0 and not visited[i-1][j]:
    tmp.append((i-1, j))
  if i < h-1 and not visited[i+1][j]:
    tmp.append((i+1, j))
  if j > 0 and not visited[i][j-1]: 
    tmp.append((i, j-1))
  if j < w-1 and not visited[i][j+1]:
    tmp.append((i, j+1))
  return tmp

N = int(input())
answers = []
for test_case in range(N):
  h, w = list(map(int, input().split()))
  map_ = []   # 지도
  keys = {}   # 습득한 key
  doors = []  # 도달한 잠긴 문 (x, y, key)
  stack = []  # 탐색용 stack
  visited = [[False]*w for _ in range(h)]
  ans = 0

  for i in range(h):
    tmp = input()
    map_.append(tmp)
    if i == 0 or i == h-1:
      for j, t in enumerate(tmp):
        ans = check(i, j, t, visited, keys, stack, ans)
    else:
      for j in [0, w-1]:
        t = tmp[j]
        ans = check(i, j, t, visited, keys, stack, ans)

  key = input()
  if key != '0':
    for k in key:
      keys[k] = True
  
  while True:
    if len(stack) > 0:
      i, j = stack.pop()
      for n_i, n_j in explore(i, j, visited):
          t = map_[n_i][n_j]
          ans = check(n_i, n_j, t, visited, keys, stack, ans)

    if len(stack) == 0:
      for idx in range(len(doors)-1, -1, -1):
        i, j, d = doors[idx]
        if keys.get(d.lower()):
          stack.append((i, j))
          visited[i][j] = True
          del doors[idx]
    
    if len(stack) == 0:
      break
    
  answers.append(ans)

for ans in answers:
  print(ans)