def solution(arr):
    last = [0, 0] # max, min
    num = []
    for a in arr[::-1]:
        if a == "+":
            continue
        elif a == "-":
            s = sum(num)
            new_max = max(-2*num[-1] + s + last[0], -s - last[1])
            new_min = min(-s - last[0], -s + last[1])
            last[0], last[1] = new_max, new_min
            
            num = []
        else:
            num.append(int(a))
    
    
    return sum(num)+last[0]