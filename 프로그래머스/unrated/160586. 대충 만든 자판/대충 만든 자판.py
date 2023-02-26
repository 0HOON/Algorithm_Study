def solution(keymap, targets):
    alphabets = {}
    for k in keymap:
        for i, c in enumerate(k):
            alphabets[c] = min(alphabets.get(c, 1000), i+1)
            
    answer = []
    for t in targets:
        tmp = 0
        for c in t:
            if alphabets.get(c):
                tmp += alphabets[c]
            else:
                tmp = -1
                break
        answer.append(tmp)
        
    return answer