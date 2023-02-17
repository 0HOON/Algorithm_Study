v, e = list(map(int, input().split()))
edges = []
for i in range(e):
  edges.append(list(map(int, input().split())))

edges = list(map(lambda x: (x[0]-1, x[1]-1, x[2]), edges))
edges = sorted(edges, key=lambda x: x[2])
spanned = [i for i in range(v)]
group = {i: [i] for i in range(v)}
g = 1
n = 0
ans = 0
for a, b, w in edges:
  if n == v-1:
    break
  g_a = spanned[a]
  g_b = spanned[b]
  if g_a != g_b:
    group[g_a].extend(group[g_b])
    for i in group[g_b]:
      spanned[i] = g_a
    del group[g_b]
    ans += w
    n += 1
  else:   
    #continue
    pass
  
print(ans)