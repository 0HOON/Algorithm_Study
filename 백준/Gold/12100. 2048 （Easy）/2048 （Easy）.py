import copy

def move_line(line, direction):
  tmp = [x for x in line if x != 0]
  result = []
  if direction == 'l' or direction == 'u':
    pop_idx = 0
  elif direction == 'r' or direction == 'd':
    pop_idx = -1
  else:
    print('DIRECTION ERROR')

  while len(tmp) > 0:
    n = tmp.pop(pop_idx)
    if len(result) > 0 and n == result[-1]:
      result[-1] = result[-1] * 2
      if len(tmp) > 0:
        result.append(tmp.pop(pop_idx))
    else:
      result.append(n)
  
  if pop_idx == 0:
    result = result + [0] * (len(line) - len(result))
  else:
    result = [0] * (len(line) - len(result)) + list(reversed(result)) 

  return result

def move(board, direction):
  b = copy.deepcopy(board)
  if direction == 'l' or direction == 'r':
    for i, row in enumerate(b):
      b[i] = move_line(row, direction)
  
  elif direction == 'u' or direction == 'd':
    for j in range(len(b)):
      col = []
      for i in range(len(b)):
        col.append(b[i][j])
      moved_col = move_line(col, direction)
      for i in range(len(b)):
        b[i][j] = moved_col[i]
        
  else:
    print('DIRECTION ERROR')
  
  return b

N = int(input())
board = []
for _ in range(N):
  board.append(list(map(int, input().split())))

stack = [(board, 0)]
ans = 0
directions = ['l', 'r', 'u', 'd']
while len(stack) > 0:
  b, n = stack.pop()
  if n == 5:
    max_block = max(map(max, b))
    if max_block > ans:
      ans = max_block
  else:
    for d in directions:
      stack.append((move(b, d), n+1))
      

print(ans)
