def get_block(n):
    if n <= 1:
        return 0
    if n > 10**7:
        max_i = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0 and max_i < i:
                max_i = i
            if n % i == 0 and max_i < n//i and n//i <= 10**7:
                max_i = n//i
        return max_i
    else:
        for i in range(n-1, int(n**0.5)-1, -1):
            if n % i == 0:
                return i
    return 1

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(get_block(i))
    return answer