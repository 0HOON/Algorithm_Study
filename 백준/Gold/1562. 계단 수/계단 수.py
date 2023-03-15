N = int(input())
memo = [[[0]*(2**10) for _ in range(10)] for __ in range(N)]

for i in range(10):
    memo[N-1][i][-1] = 1

# idx 번째 자리수가 n이고 mask만큼 숫자를 사용했을 때 계단 수 개수

def dfs(memo, idx, n, mask):
    if memo[idx][n][mask] or idx == len(memo)-1:
        return memo[idx][n][mask]

    ans = 0
    if n < 9:
        ans += dfs(memo, idx+1, n+1, mask | 2**(n+1))
    
    if n > 0:
        ans += dfs(memo, idx+1, n-1, mask | 2**(n-1))
    
    memo[idx][n][mask] = ans % 1000000000
    return memo[idx][n][mask]

ans = 0
for i in range(1, 10):
    ans = (ans + dfs(memo, 0, i, 2**i)) % 1000000000

print(ans)