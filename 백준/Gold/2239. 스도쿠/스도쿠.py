board = []
for i in range(9):
  board.append(list(map(int, input())))

row = {i:[False]*9 for i in range(9)}
col = {i:[False]*9 for i in range(9)}
block = {i:[False]*9 for i in range(9)}
blank = []

for i in range(9):
  for j in range(9):
    n = board[i][j]-1
    if n != -1:
      row[i][n] = True
      col[j][n] = True
      b = i//3 * 3 + j//3
      block[b][n] = True
    else:
      blank.append((i, j))

def fill_blank(n):
  i, j = blank[n]
  blk = i//3 * 3 + j//3
  used = list(map(lambda x: x[0] or x[1] or x[2], zip(row[i], col[j], block[blk])))
  for num, u in enumerate(used):
    if not u:
      board[i][j] = num+1
      row[i][num] = True
      col[j][num] = True
      block[blk][num] = True

      if n == len(blank)-1:
        return True, board

      success, brd = fill_blank(n+1)
      if success:
        return True, brd
      else:
        board[i][j] = 0
        row[i][num] = False
        col[j][num] = False
        block[blk][num] = False

  return False, None

_, b = fill_blank(0)
for r in b:
  print(''.join(list(map(str, r))))