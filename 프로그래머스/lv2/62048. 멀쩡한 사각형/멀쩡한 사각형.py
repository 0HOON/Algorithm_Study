def num_rec(w, h):
    # w < h
    for i in range(1, w+1):
        if abs((h/w * i) - ((h*i)//w)) < 0.0000001:
            break
    return w*h - (w+h-1-(w//i - 1))
    
def solution(w,h):
    w, h = sorted((w, h))
    answer = num_rec(w, h)
    return answer