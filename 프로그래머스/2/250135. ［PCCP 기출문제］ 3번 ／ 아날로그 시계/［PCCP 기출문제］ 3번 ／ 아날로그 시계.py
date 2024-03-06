def hms2s(h, m, s):
    return h*3600 + m*60 + s

def t2d(s, dps):
    d = s*dps
    _, d = divmod(d, 360)
    return d

def is_ahead(a, b):
    # a가 b보다 앞(왼)쪽 180도에 있는지
    return ((a-b) % 360)> 180
    
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = hms2s(h1, m1, s1)
    end = hms2s(h2, m2, s2)
    
    dps_h = 360/(3600*12)
    dps_m = 360/3600
    dps_s = 360/60
    
    prev_hh = t2d(start, dps_h)
    prev_mh = t2d(start, dps_m)
    prev_sh = t2d(start, dps_s)
    if prev_sh == prev_hh:
        answer += 1
    if prev_sh == prev_mh:
        answer += 1
        if prev_sh == prev_hh:
            answer -= 1
    
    tmp = 10
    for t in range(start+1, end+1):
        hh = t2d(t, dps_h)
        mh = t2d(t, dps_m)
        sh = t2d(t, dps_s)
        if is_ahead(prev_sh, prev_hh) and not is_ahead(sh, hh):
            answer += 1
            
        if is_ahead(prev_sh, prev_mh) and not is_ahead(sh, mh):
            answer += 1
            # prev_hh + tt*dps_h = prev_sh + tt*dps_s
            tt = (prev_sh-prev_hh)/(dps_h-dps_s)
            print(prev_mh + tt*dps_m, prev_sh + tt*dps_s)
            if abs((prev_mh + tt*dps_m) - (prev_sh + tt*dps_s))< 1e-9:
                answer -= 1     
        prev_sh, prev_mh, prev_hh = sh, mh, hh
            
    return answer