# 9465 스티커 실버1

T = int(input())

for t in range(T):
  n = int(input())
  ss = []
  ss.append([0, 0] + list(map(int, input().split())))
  ss.append([0, 0] + list(map(int, input().split())))

  for i in range(2, n + 2):
    ss[0][i] += max(ss[1][i - 1], ss[1][i - 2])
    ss[1][i] += max(ss[0][i - 1], ss[0][i - 2])

  print(max(ss[0][-1], ss[1][-1]))