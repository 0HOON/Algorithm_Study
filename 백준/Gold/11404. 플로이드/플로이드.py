n = input()
n = int(n)
m = input()
m = int(m)

dist = [[float('inf')]*n for _ in range(n)]
for i in range(n):
  dist[i][i] = 0

for _ in range(m):
  a, b, c = (list(map(int, input().split())))
  if c < dist[a-1][b-1]:
    dist[a-1][b-1] = c

for i in range(n):
  tmp = dist[i]
  for j, d in enumerate(dist):
    if j == i:
      continue

    for k, dd in enumerate(d):
      if d[i] + tmp[k] < dd:
        d[k] = d[i] + tmp[k]

for i in range(n):
  for j in range(n):
    if dist[i][j] == float('inf'):
      dist[i][j] = 0
      
for d in dist:  
  print(' '.join(list(map(str,d))))