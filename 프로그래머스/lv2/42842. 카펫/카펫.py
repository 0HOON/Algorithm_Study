def solution(brown, yellow):
    for i in range(int(yellow**0.5)):
        r = i+1
        c = yellow//r
        if yellow % r == 0:
            b = (r+2)*2 + (c+2)*2 - 4
            if b == brown:
                return [c+2, r+2]
