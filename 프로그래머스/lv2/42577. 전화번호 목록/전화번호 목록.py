def solution(phone_book):
    answer = True
    book = {}
    for phone_num in phone_book:
        b = book
        p = True
        for i, n in enumerate(phone_num):
            if p and i > 0 and b.get(n) == None and len(b) == 0: 
                print(phone_num, i, n, b)
                return False
            elif b.get(n) == None:
                b[n] = {}
                p = False
            b = b[n]
        if len(b) > 0:
            print(phone_num, b)
            return False
            
    return answer