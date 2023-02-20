from itertools import accumulate

N, S = list(map(int, input().split()))
seq = [0] + list(accumulate(map(int, input().split())))

if seq[-1] < S:
  print(0)
else:
  i = 0
  j = 1
  min_len = N
  while i < N and j < N+1: 
    s = seq[j]-seq[i]
    if s < S:
      j += 1
    else:
      if j-i < min_len:
        min_len = j-i
      i += 1
  print(min_len)