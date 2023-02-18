import sys
import heapq

n, k = list(map(int, sys.stdin.readline().split()))

bj = []
for i in range(n):
  bj.append(list(map(int, sys.stdin.readline().split()))) 
for i in range(k):
  bj.append([int(sys.stdin.readline()), float('inf')])

bj = sorted(bj)

ans = 0
q = []
for m, v in bj:
  if v != float('inf'):
    heapq.heappush(q, -v)
  else:
    if len(q) > 0:
      ans += - heapq.heappop(q)

print(ans)