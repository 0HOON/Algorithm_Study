def find_idx(a, b, n, seq):
  if a == b:
    return a
  m = (a+b)//2
  if n == seq[m]:
    return m
  elif n > seq[m]:
    return find_idx(m+1, b, n, seq)
  else:
    return find_idx(a, m, n, seq)

N = int(input())
seq = list(map(int, input().split()))
las = [seq[0]]
for s in seq[1:]:
  if s > las[-1]:
    las.append(s)
  else:
    i = find_idx(0, len(las)-1, s, las)
    las[i] = s

print(len(las))