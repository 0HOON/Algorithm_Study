def str2s(s):
    hh, mm, ss = s.split(':')
    return 3600*1000*int(hh) + 60*1000*int(mm) + int(1000*float(ss))

def solution(lines):
    start_t = []
    end_t = []
    N = len(lines)
    
    for l in lines:
        _, t, d = l.split()
        e = str2s(t)
        start_t.append(e-int(1000*float(d[:-1]))+1)
        end_t.append(e)
    
    start_t = sorted(start_t)
    s_i = 0
    e_i = 0
    max_n = 1
    n = 0
    while s_i < N and e_i < N:
        s = start_t[s_i]
        e = end_t[e_i]
        if s-999 <= e:
            s_i += 1
            n += 1
            if n > max_n:
                max_n = n
        else:
            e_i += 1
            n -= 1
            
    return max_n