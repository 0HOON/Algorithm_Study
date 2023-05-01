def compress(arr):
    l = len(arr)
    m = l//2
    if l == 1:
        if arr[0][0] == 0:
            return (1, 0)
        else:
            return (0, 1)
    
    a1, a2, a3, a4 = [], [], [], []
    total = 0
    for i, r in enumerate(arr):
        total += sum(r)
        if i < m:
            a1.append(r[:m])
            a2.append(r[m:])
        else:
            a3.append(r[:m])
            a4.append(r[m:])
    if total == 0:
        return (1, 0)
    elif total == l*l:
        return (0, 1)
    
    else:
        zeros = 0
        ones = 0
        for a in [a1, a2, a3, a4]:
            z, o = compress(a)
            zeros += z
            ones += o
        return (zeros, ones)
    
def solution(arr):
    answer = compress(arr)
    return list(answer)