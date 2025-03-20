def check(a, b, g, s, w, t, time):
    total_w = 0
    total_g = 0
    total_s = 0
    
    for gg, ss, ww, tt in zip(g, s, w, t):
        count = ((time//tt)+1)//2
        total_w += min(ww * count, gg+ss)
        total_g += min(ww * count, gg)
        total_s += min(ww * count, ss)
    
    return total_w >= (a+b) and total_g >= a and total_s >= b
        
def solution(a, b, g, s, w, t):
    l = 0
    r = (1e5*2) * 1 * (2 * 1e9)
    while l < r-1:
        m = (l+r)//2
        if check(a, b, g, s, w, t, m):
            r = m
        else:
            l = m
    
    return r