def n2b(s):
    res = ''
    while s > 0:
        if s & 1:
            res = '1' + res
        else:
            res = '0' + res
        s = s >> 1
    return res

def sol(s):
    ans = 0
    num = 0
    while s != '1':
        l = len(s)        
        ones = len(''.join(s.split('0')))
        zeros = l-ones
        ans += zeros
        num += 1
        s = n2b(ones)
    return [num, ans]
        
def solution(s):
    answer = sol(s)
    return answer