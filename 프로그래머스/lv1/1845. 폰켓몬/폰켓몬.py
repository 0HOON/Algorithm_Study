def solution(nums):
    answer = 0
    memo = {}
    for n in nums:
        if memo.get(n, False):
            continue
        else:
            memo[n] = True
            answer += 1
        if answer >= len(nums)//2:
            return answer
    return answer