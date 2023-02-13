# 11053
def find_idx(n, seq, s, e):
  while s < e:
    m = (s+e) // 2
    if seq[m] == n:
      return m
    elif seq[m] < n:
      s = m+1
    else:
      e = m
  return e

n = input()
seq = list(map(int, input().split()))

ans = [seq[0]]

for s in seq:
  if s > ans[-1]:
    ans.append(s)
  elif s < ans[-1]:
    idx = find_idx(s, ans, 0, len(ans)-1)
    ans[idx] = s
    
  
print(len(ans))