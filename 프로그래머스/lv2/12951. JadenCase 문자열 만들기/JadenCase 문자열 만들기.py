def JadenCase(s):
    res = ''
    for i, ss in enumerate(s):
        if i == 0 and ss.isalpha():
            res += ss.upper()
        elif ss.isalpha():
            res += ss.lower()
        else:
            res += ss
            
    return res

def solution(s):
    answer = ''
    isfirst = True
    for ss in s:
        if isfirst and ss.isalpha():
            answer += ss.upper()
            isfirst = False
        elif ss.isalpha():
            answer += ss.lower()
        elif ss != ' ':
            answer += ss
            isfirst = False
        elif ss == ' ':
            answer += ss
            isfirst = True
    return answer