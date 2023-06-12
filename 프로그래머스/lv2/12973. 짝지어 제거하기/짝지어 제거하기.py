from collections import deque
def solution(s):
    stack = deque([])
    for ss in s:
        if len(stack) > 0 and stack[-1] == ss:
            stack.pop()
        else:
            stack.append(ss)
    
    return int(len(stack)==0)