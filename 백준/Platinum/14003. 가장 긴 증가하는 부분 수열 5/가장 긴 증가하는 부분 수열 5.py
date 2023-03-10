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
seq_ = [0] * len(seq)
last = 0
for idx in range(1, len(seq)):
  s = seq[idx]
  if s > las[-1]:
    last = idx
    seq_[idx] = len(las)
    las.append(s)
  else:
    i = find_idx(0, len(las)-1, s, las)
    las[i] = s
    seq_[idx] = i

print(len(las))
las_ = [str(seq[last])]
l = len(las)-1
for i in range(last, -1, -1):
  if seq_[i] == l - 1:
    las_.append(str(seq[i]))
    l -= 1
print(' '.join(reversed(las_)))