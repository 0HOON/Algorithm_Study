# 나눗셈에서 float으로 변환 -> 유효숫자 15자리로 손실 생길 수 있음
# / 대신 //으로 정확한 계산 가능.
N = 1000000007

def fibo(n, memo):
  if n < 2:
    return n

  if memo.get(n, -1) > 0:
    return memo[n]

  if n % 2 == 0:
    m = n//2
    a = fibo(m, memo) 
    b = fibo(m - 1, memo) 
    memo[n] = ((2*b + a) * a) % N
    return memo[n]
  else:
    m = (n-1)//2
    a = fibo(m, memo)
    b = fibo(m + 1, memo)
    memo[n] = ((a**2) + (b**2)) % N
    return memo[n]

num = input()
num = int(num)
memo = {}

print(fibo(num, memo))