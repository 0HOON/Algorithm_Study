def solution(a, b, n):
    answer = 0
    empty = n
    while empty >= a:
        empty -= a
        empty += b
        answer += b
            
    return answer