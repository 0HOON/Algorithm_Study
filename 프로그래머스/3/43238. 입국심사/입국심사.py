def solution(n, times):
    l = 0
    r = 1e9*1e9+1
    while l+1 < r:
        m = (l+r)//2
        if is_possible(m, n, times):
            r = m
        else:
            l = m 
    return r

def is_possible(time, n, times):
    possible_n = 0
    for t in times:
        possible_n += time // t
    return possible_n >= n