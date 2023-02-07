def split_s(s):
    x = s[0]
    t = 0
    for i, c in enumerate(s):
        if c == x:
            t += 1
        else:
            t -= 1
        
        if t == 0:
            return s[i+1:]
    return ''
def solution(s):
    answer = 0
    while len(s) > 0:
        s = split_s(s)
        answer += 1
    return answer