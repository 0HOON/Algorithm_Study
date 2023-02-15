# 구간 합 구하기.
import sys
from operator import add

n, m = list(map(int, sys.stdin.readline().split()))
table = [[0]*(n+1)]
cumsum = {}

for _ in range(n):
  tmp = 0
  row = [0]
  for num in list(map(int, sys.stdin.readline().split())):
    tmp += num
    row.append(tmp)
  table.append(row)

tmp = [0]*(n+1)
for i, t in enumerate(table):
  tmp = list(map(add, tmp, t))
  table[i] = tmp

ans = []
for _ in range(m):
  x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
  ans.append(str(table[x2][y2] - table[x1-1][y2] - (table[x2][y1-1] - table[x1-1][y1-1])))

print(' '.join(ans))
