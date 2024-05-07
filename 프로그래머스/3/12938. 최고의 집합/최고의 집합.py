def solution(n, s):
    if n > s:
        return [-1]
    answer = []
    d, r = divmod(s, n)
    answer = [d]*(n-r) + [d+1]*r 
    return answer