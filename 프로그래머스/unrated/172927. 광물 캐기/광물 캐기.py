def Fatigue(pick, minerals):
    pm = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    p = pm[pick]
    res = 0
    for i, m in enumerate(minerals):
        res += p[i]*m
    return res
    
        
def solution(picks, minerals):
    answer = 0
    m = []
    i = 0
    max_len = sum(picks) * 5
    while i < max_len:
        dia = 0
        iron = 0
        stone = 0
        next_i = min(i+5, max_len)
        for mineral in minerals[i:next_i]:
            if mineral == 'diamond':
                dia += 1
            elif mineral == 'iron':
                iron += 1
            elif mineral == 'stone':
                stone += 1
        m.append((dia, iron, stone))
        i = next_i
    
    m = sorted(m)
    while len(m) > 0:
        tmp = m.pop(-1)
        if picks[0] > 0:
            pick = 0
            picks[0] -= 1
        elif picks[1] > 0:
            pick = 1
            picks[1] -= 1
        elif picks[2] > 0:
            pick = 2
            picks[2] -= 1
            
        answer += Fatigue(pick, tmp)
        
    return answer