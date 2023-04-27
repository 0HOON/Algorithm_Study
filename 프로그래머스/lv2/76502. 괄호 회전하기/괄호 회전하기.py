from collections import deque
def check(s):
    q = deque([])
    memo = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    for ss in s:
        if len(q) == 0 or q[-1] != memo.get(ss):
            q.append(ss)
        else:
            q.pop()
    return len(q) == 0

def solution(s):
    answer = 0
    tmp = s
    memo = {}
    for n in range(len(s)):
        tmp = tmp[1:] + tmp[0]
        if memo.get(tmp) != None:
            answer += memo[tmp]
            continue
        
        memo[tmp] = check(tmp)
        answer += memo[tmp]
    return answer