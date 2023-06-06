def num_1(n):
    a, b = 1, 1
    n_1 = 0
    while a>0:
        a, b = divmod(n, 2)
        n_1 += b==1
        n = (n-b)//2
    return n_1

def solution(n):
    n_1 = num_1(n)
    tmp_n = 0
    while tmp_n != n_1:
        n += 1
        tmp_n = num_1(n)
        
    return n