from itertools import combinations

N, S = list(map(int, input().split()))

seq = list(map(int, input().split()))

sl = seq[:N//2]
sr = seq[N//2:]

left = {0: 1}
right = {0: 1}

for i in range(len(sl)):
  for tmp in combinations(sl, i+1):
    s = sum(tmp)
    left[s] = left.get(s, 0) + 1

for i in range(len(sr)):
  for tmp in combinations(sr, i+1):
    s = sum(tmp)
    right[s] = right.get(s, 0) + 1

left = sorted(left.items())
right = sorted(right.items(), reverse=True)

i = 0
j = 0
ans = 0
while i < len(left) and j < len(right):
  l = left[i]
  r = right[j]
  s = l[0] + r[0]
  if s == S:
    ans += l[1] * r[1]
    i += 1
    j += 1
  elif s > S:
    j += 1
  elif s < S:
    i += 1

if S == 0:
  ans -= 1
  
print(ans)