# 1149 RGB거리 실버1

from cmath import inf

N = input()
costs = []
for i in range(int(N)):
    costs.append(list(map(lambda x: int(x), input().split())))

for i in range(len(costs)-2, -1, -1):
    for j in range(3):
        min_after = inf
        for k in range(3):
            if k == j:
                continue
            if costs[i+1][k] < min_after:
                min_after = costs[i+1][k]
        
        costs[i][j] += min_after

print(min(costs[0]))