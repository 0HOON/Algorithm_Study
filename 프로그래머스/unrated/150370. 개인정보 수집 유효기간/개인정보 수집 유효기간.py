def date_add(date, month):
    y, m, d = list(map(int, date.split('.')))
    d = d - 1
    if d == 0:
        d = 28
        m = m - 1
    m = m + month
    while m > 12:
        m = m - 12
        y = y + 1
        
    y = str(y)
    
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
        
    if d < 10:
        d = '0' + str(d)
    else:
        d = str(d)
        
    return '.'.join([y, m, d])

def date_compare(a, b):
    # a < b 인지 검사
    aa = int(''.join(a.split('.')))
    bb = int(''.join(b.split('.')))
    
    return aa < bb
    

def solution(today, terms, privacies):
    terms_dict = {}
    for term in terms:
        name, t = term.split()
        terms_dict[name] = int(t)
    
    answer = []
    for i, p in enumerate(privacies):
        date, term = p.split()
        expire = date_add(date, terms_dict[term])
        if date_compare(expire, today):
            answer.append(i+1)
    
    return answer