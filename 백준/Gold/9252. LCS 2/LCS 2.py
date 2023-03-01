a = input()
b = input()
table = [[''] * len(b) for _ in range(len(a))]

for i in range(len(a)):
  for j in range(len(b)):
    if j == 0:
      if a[i] == b[j]:
        table[i][j] = a[i]
      elif i > 0:
        table[i][j] = table[i-1][j]
      continue
    if i == 0:
      if a[i] == b[j]:
        table[i][j] = a[i]
      else:
        table[i][j] = table[i][j-1]
      continue
    
    l = table[i][j-1]
    u = table[i-1][j]
    if a[i] == b[j]:
      diag = table[i-1][j-1] + a[i]
      table[i][j] = max(l, u, diag, key=len)
    else:
      table[i][j] = max(l, u, key=len)

ans = table[-1][-1]
print(len(ans))
if len(ans) > 0:
  print(ans)