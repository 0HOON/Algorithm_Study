def solution(n):
    # 여는 괄호의 수가 닫는 괄호의 수보다 많아지지 않도록.
    answer = 0
    a = [0, 1]
    for i in range(2, n*2+1):
        b = [0 for _ in range(i+1)]
        for ii, aa in enumerate(a):
            if ii > 0:
                b[ii-1] += aa
            if ii < i:
                b[ii+1] += aa
        a = b
    
    return a[0]