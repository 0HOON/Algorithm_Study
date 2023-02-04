#2407 조합 실버3
from math import factorial

n, m = list(map(int, input().split()))
ans = 1
m = min(n-m, m)
ans = factorial(n)//(factorial(n-m) * factorial(m))
print(int(ans))