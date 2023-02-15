n, k = list(map(int, input().split()))
queue = [(n, 0)]
dist = [-1]*100001
while True:
  p, d = queue.pop(0)
  dist[p] = d
  if p == k:
    break
  if p*2 <= len(dist)-1 and dist[p*2] < 0:
    queue = [(p*2, d)] + queue
  if p > 0 and dist[p-1] < 0:
    queue.append((p-1, d+1))
  if p < len(dist)-1 and dist[p+1] < 0:
    queue.append((p+1, d+1))

print(dist[k])