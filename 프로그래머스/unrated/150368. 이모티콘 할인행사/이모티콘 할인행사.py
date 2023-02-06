def check(u, emoticons, sale):
    min_sale = u[0]
    max_price = u[1]
    total_price = 0
    plus = False
    for i, s in enumerate(sale):
        if s*10 >= min_sale:
            total_price += emoticons[i] * (1-s/10)
        if total_price >= max_price:
            plus = True
            total_price = 0
            break
    
    return plus, total_price
    
def next_sale(sale):
    for i in range(len(sale)):
        sale[i] += 1
        if sale[i] > 4:
            sale[i] = 1
            continue
        break
    return sale

def solution(users, emoticons):
    answer = [0, 0]
    sale = [1] * len(emoticons)
    
    for _ in range(4**len(emoticons)):
        total_plus = 0
        total_price = 0
        for u in users:
            plus, price = check(u, emoticons, sale)
            total_plus += plus
            total_price += price

        if total_plus > answer[0]:
            answer[0] = total_plus
            answer[1] = total_price
        elif total_plus == answer[0] and total_price > answer[1]:
            answer[0] = total_plus
            answer[1] = total_price
        sale = next_sale(sale)

    return answer