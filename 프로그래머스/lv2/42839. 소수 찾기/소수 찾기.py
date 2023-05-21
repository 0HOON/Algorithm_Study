from itertools import permutations

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1):
        if i % 2 == 0:
            continue
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    checked = {}
    for i in range(1, len(numbers)+1):
        for n in permutations(numbers, i):
            num = int(''.join(n))
            if checked.get(num, False):
                continue
            answer += isPrime(num)
            checked[num] = True
    return answer