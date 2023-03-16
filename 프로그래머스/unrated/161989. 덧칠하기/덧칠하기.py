def paint(idx, m, section):
    i = idx
    while i < idx+m and i < len(section):
        section[i] = False
        i += 1
    
def solution(n, m, section):
    answer = 0
    s = [False] * n
    for sec in section:
        s[sec-1] = True
        
    for i, need_paint in enumerate(s):
        if need_paint:
            paint(i, m, s)
            answer += 1
    
    return answer