def compressed_len(s, n):
    tmp = ''
    tmp_n = 1
    res = ''
    for i in range(len(s)//n+1):
        idx = slice(i*n, (i+1)*n)
        if s[idx] == tmp:
            tmp_n += 1
        else:
            if tmp_n == 1:
                res += tmp
            else:
                res += str(tmp_n) + tmp
            tmp = s[idx]
            tmp_n = 1
    if tmp_n == 1:
        res += tmp
    else:
        res += str(tmp_n) + tmp
    return len(res)

def solution(s):
    answer = 10000
    for i in range(len(s)//2+1):
        answer = min(answer, compressed_len(s, i+1))
    return answer