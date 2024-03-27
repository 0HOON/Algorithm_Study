def solution(n):
    answer = ''
    number = ['1', '2', '4']
        
    while n > 0:
        n -= 1
        n, r = divmod(n, 3)
        answer = number[r] + answer
        
    return answer