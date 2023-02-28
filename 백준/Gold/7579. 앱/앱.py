# memo[cost] : cost 이용 시 최대 확보 가능 mem

def update_memo(n):
  tmp = list(memo.items())
  for c, m in tmp:
    memo[c+cost[n]] = max(memo.get(c+cost[n], 0), m + mem[n])

  memo[cost[n]] = max(memo.get(cost[n], 0), mem[n])


N, M = list(map(int, input().split()))
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

memo = {}

for i in range(N):
  update_memo(i)

for c, m in sorted(memo.items()):
  if m >= M:
    print(c)
    break
