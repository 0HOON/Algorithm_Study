from itertools import combinations
from math import sqrt
def SumVectorLen(X, Y, indices):
    sum_x = sum(X)
    sum_y = sum(Y)
    
    for i in indices:
        sum_x -= 2*X[i]
        sum_y -= 2*Y[i]

    return sqrt(sum_x**2 + sum_y**2)

T = int(input())
answers = []
for _ in range(T):
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)

    ans = float('inf')
    for l in combinations(range(N), N//2):
        tmp = SumVectorLen(X, Y, l)
        ans = min(ans, tmp)

    answers.append(ans)

for ans in answers:
    print(ans)