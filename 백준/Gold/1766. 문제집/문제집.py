N, M = list(map(int, input().split()))

need_to_solve = [0 for _ in range(N+1)]
children = {}
solved = [True] + [False for _ in range(N)]
for _ in range(M):
  a, b = list(map(int, input().split()))
  need_to_solve[b] += 1
  children[a] = children.get(a, []) + [b]

ans = []

for _ in range(N):
  for i, (s, n) in enumerate(zip(solved, need_to_solve)):
    if (not s) and (n == 0):
      solved[i] = True
      for q in children.get(i, []):
        need_to_solve[q] -= 1
      ans.append(str(i))
      break

print(' '.join(ans))