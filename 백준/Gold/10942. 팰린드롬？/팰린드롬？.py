def ispalindrome(a, b, memo, nums):
  if memo[a][b] != -1:
    return memo[a][b]
  
  if a >= b:
    return 1

  if nums[a] == nums[b]:
    memo[a][b] = ispalindrome(a+1, b-1, memo, nums)
    return memo[a][b]
  
  else:
    memo[a][b] = 0
    return memo[a][b]

import sys

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
questions = []
memo = [[-1]*len(nums) for _ in range(len(nums))]

for i in range(M):
  print(ispalindrome(*map(lambda x: int(x)-1, sys.stdin.readline().split()), memo, nums))