def solution(cap, n, deliveries, pickups):
    answer = 0
    dlv_left = sum(deliveries)
    pck_left = sum(pickups)
    
    dlv = []
    for i, d in enumerate(deliveries):
        if d > 0:
            dlv.append([i+1, d])
    
    pck = []
    for i, p in enumerate(pickups):
        if p > 0:
            pck.append([i+1, p])
    
    while dlv_left > 0 or pck_left > 0:
        if dlv_left == 0:
            answer += 2 * pck[-1][0]
        elif pck_left == 0:
            answer += 2 * dlv[-1][0]
        else:
            answer += 2 * max(dlv[-1][0], pck[-1][0])
        
        n_dlv = min(dlv_left, cap)
        dlv_left -= n_dlv
        
        n_pck = 0
        
        # 배달
        while n_dlv > 0:
            if dlv[-1][1] > n_dlv:
                dlv[-1][1] -= n_dlv
                n_dlv = 0
            else:
                n_dlv -= dlv[-1][1]
                del dlv[-1]
        # 수거
        while n_pck < cap and len(pck) > 0:
            if pck[-1][1] > cap - n_pck:
                pck[-1][1] -= cap - n_pck
                n_pck = cap
            else:
                n_pck += pck[-1][1]
                del pck[-1]
                
        pck_left -= n_pck
        
    return answer