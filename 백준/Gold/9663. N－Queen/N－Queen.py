def check(board, n, done):
  ans = 0
  for i in range(n):
    tmp = 1 << i
    valid = True
    if done[i]:
      continue

    for j, row in enumerate(reversed(board)):
      mask = 0
      if i-j-1 >= 0:
        mask += 2**(i-j-1)
      if i+j+1 < n:
        mask += 2**(i+j+1)
      if (row & mask) > 0:
        valid = False
        break
    
    if valid:
      if len(board) == n-1:
        return 1
      else:
        done[i] = True
        if len(board) > 0:
          ans += check([*board, tmp], n, done)
        else:
          ans += check([tmp], n, done)
        done[i] = False

  return ans


n = input()
n = int(n)
done = [False] * n
print(check([], n, done))
