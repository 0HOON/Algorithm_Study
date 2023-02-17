def get_construction_time(n, time, required):
  if required[n][0] == -1:
    max_t = 0
    for r in required[n][1:]:
      t = get_construction_time(r, time, required)
      if max_t < t:
        max_t = t
    required[n][0] = max_t + time[n]
  
  return required[n][0]
  

t = int(input())
ans = []
for _ in range(t):
  n, k = list(map(int, input().split()))
  time = list(map(int, input().split()))
  required = {i: [-1] for i in range(n)}

  for i in range(k):
    a, b = list(map(int, input().split()))
    required[b-1].append(a-1)

  ans.append(get_construction_time(int(input())-1, time, required))

for a in ans:
  print(a)