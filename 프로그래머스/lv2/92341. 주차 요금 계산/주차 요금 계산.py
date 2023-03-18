def ConvertTime(t):
    h, m = list(map(int, t.split(':')))
    return h * 60 + m

def Fee(fees, t):
    f = 0
    if t <= fees[0]:
        f = fees[1]
    else:
        f += fees[1]
        t -= fees[0]
        f += fees[3] * ((t//fees[2]) + ((t%fees[2]) > 0))
    return f

def solution(fees, records):
    answer = []
    cars = {}
    for r in records:
        t, n, c = r.split()
        t = ConvertTime(t)
        n = int(n)
        if c == "IN":
            cars[n] = cars.get(n, []) + [t]
        else:
            cars[n].append(t)
            
    for c in cars:
        if len(cars[c]) % 2 == 1:
            cars[c].append(ConvertTime('23:59'))
            
    for c in cars:
        tmp = []
        for i, t in enumerate(cars[c]):
            if i % 2 == 0:
                tmp.append(cars[c][i+1] - t)
                
        cars[c] = sum(tmp)
        
    for c in sorted(cars):
        answer.append(Fee(fees, cars[c]))
    
    return answer