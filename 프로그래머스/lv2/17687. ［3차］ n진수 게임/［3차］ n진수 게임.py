# n진수 변환
# 하나씩 끊기
# 찾기
def toN(num, n):
    tmp = []
    if num == 0:
        return ['0']
    
    while True:
        if num == 0:
            break
        q, r = divmod(num, n)
        tmp.append(r)
        num = q
    
    tmp = list(map(lambda x: chr(ord('A')+x%10) if x >= 10 else str(x), tmp[::-1]))
    return tmp

def solution(n, t, m, p):
    answer = ''
    txt = ''
    idx = p-1
    i = 0
    while len(answer) < t:
        while idx > len(txt)-1:
            txt += ''.join(toN(i, n))
            i += 1
        answer += txt[idx]
        
        idx = idx + m
    return answer