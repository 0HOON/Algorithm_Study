from collections import deque

def is_correct(v):
    stack = deque([])    
    for p in v:
        if p == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(p)
            
    return len(stack) == 0

def fix(p):
    if is_correct(p):
        return p
    
    tmp = 0
    l = 0
    r = 0
    for i in range(len(p)):
        pp = p[i]
        if pp == '(':
            l += 1
        else:
            r += 1
        if l == r:
            tmp = i
            break
            
    u = p[:tmp+1]                
    v = p[tmp+1:]
    
    if is_correct(u):
        return u + fix(v)
        #return u
    else:
        res = '('
        res += fix(v)
        res += ')'
        for p in u[1:-1]:
            if p == '(':
                res += ')'
            else:
                res += '('
        return res
        
def solution(p):
    answer = fix(p)
    return answer