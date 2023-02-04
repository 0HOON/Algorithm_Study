# 1932 정수 삼각형 실버1
N = int(input())

d = [0] * (N+1)
for i in range(N):
    n = list(map(int, input().split()))
    new_d = d.copy()
    new_d[0] = d[0] + n[0]
    for j in range(1, i):
        new_d[j] = max(d[j] + n[j], d[j-1] + n[j])
    new_d[i] = d[i-1] + n[i]
    d = new_d
print(max(new_d))