from itertools import combinations
def CumSum(l):
  tmp = 0
  res = [0]
  i = 0
  while i < len(l):
    tmp += l[i]
    res.append(tmp)
    i += 1
  
  return res

memoA = {}
memoB = {}

T = int(input())
N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

cumA = CumSum(A)
cumB = CumSum(B)

for a, b in combinations(cumA, 2):
  memoA[b-a] = memoA.get(b-a, 0) + 1

for a, b in combinations(cumB, 2):
  memoB[b-a] = memoB.get(b-a, 0) + 1

ans = 0
if len(memoA) < len(memoB):
  for key in memoA:
    if memoB.get(T-key, 0):
      ans += memoA[key] * memoB[T-key]
else:
  for key in memoB:
    if memoA.get(T-key, 0):
      ans += memoA[T-key] * memoB[key]

print(ans)