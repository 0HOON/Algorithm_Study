# 1167 트리의 지름 골드3

def get_max_distance(f, v):
  max_d = 0
  max_v = v
  vv = mm[v] 
  for i in range(int(len(vv) / 2)):
    next = vv[i*2]
    if next != f:
      new_d, new_v = get_max_distance(v, next)
      new_d += vv[i*2 + 1]
      if new_d > max_d:
        max_d = new_d
        max_v = new_v
  
  return max_d, max_v

V = int(input())

mm = [None] * (V+1)

for i in range(int(V)):
  vv = list(map(int, input().split()))
  mm[vv[0]] = vv[1:-1]

dd, vv = get_max_distance(None, 1)
dd, vv = get_max_distance(None, vv)
print(dd)