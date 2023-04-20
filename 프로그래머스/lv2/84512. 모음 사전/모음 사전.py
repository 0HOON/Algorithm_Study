def solution(word):
    answer = 0
    memo = {c: i for i, c in enumerate(['A', 'E', 'I', 'O', 'U'])}
    
    for i, c in enumerate(word):
        tmp = 0
        for t in range(5-i):
            tmp += 5**t
        tmp = tmp * memo[c]
        answer += tmp+1
        
    return answer