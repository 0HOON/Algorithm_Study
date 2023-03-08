N = int(input())
memo = [float('inf')] * (N+1)
memo[N] = 0
q = [(N, 0)]
while len(q) > 0:
    num, n = q.pop(0)
    if num == 1:
        continue
    if num % 3 == 0 and n+1 < memo[num//3]:
        q.append((num//3, n+1))
        memo[num//3] = n+1
    if num % 2 == 0 and n+1 < memo[num//2]:
        q.append((num//2, n+1))
        memo[num//2] = n+1
    if n+1 < memo[num-1]:
        q.append((num-1, n+1))
        memo[num-1] = n+1

print(memo[1])
num = 1
nums = []
n = memo[1]
while True:
    nums.append(str(num))
    if num == N:
        break
    if num*3 <= N and memo[num*3] == n-1:
        n -= 1
        num = num*3
    elif num*2 <= N and memo[num*2] == n-1:
        n -= 1
        num = num*2
    elif num+1 <= N:
        n -= 1
        num = num+1
print(' '.join(nums[::-1]))