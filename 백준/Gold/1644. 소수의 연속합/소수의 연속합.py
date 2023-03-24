from math import sqrt

def IsPrime(n, p_list):
  for p in p_list:
    if p > sqrt(n):
      break
    if n%p == 0:
      return False
  return True

def GetPrimeList(n):
  p_list = [2]
  p = 3
  while p <= n:
    if IsPrime(p, p_list):
      p_list.append(p)
    p += 2

  return p_list

N = int(input())
p_list = GetPrimeList(N)
p_cumsum = [0]
tmp = 0
for p in p_list:
  tmp += p
  p_cumsum.append(tmp)

ans = 0

j = len(p_cumsum)-1
i = j-1

while i >= 0 and j > i:
  s = p_cumsum[j] - p_cumsum[i]
  if s == N:
    ans += 1
    i -= 1
    j -= 1
  elif s < N:
    i -= 1
  elif s > N:
    j -= 1

print(ans)