from collections import deque
def solution(number, k):
    number = list(map(int, number))
    answer = deque([])
    kk = k
    n9 = 0
    for n in number:
        if len(answer) == 0:
            answer.append(n)
            continue
            
        tmp = 0
        
        if n > 0:
            for i in range(-min(len(answer), kk), 0):
                a = answer[i]
                if a < n:
                    tmp = -i
                    break
                
        if tmp > 0:
            kk -= tmp
            for _ in range(tmp):
                answer.pop()
            answer.append(n)
            
        elif len(answer) < len(number)-k:
            answer.append(n)
        
        for i, a in enumerate(answer):
            if a != 9:
                for _ in range(i):
                    answer.popleft()
                n9 += i
                break
                
    return '9'*n9 + ''.join(list(map(str, answer)))