from collections import deque

def count(m):
    ans = 0
    
    for k in m:
        q = deque([(m[k], 1, 1)])
        while len(q) > 0:
            mm, step, l = q.popleft()
            if mm == True:
                ans += step
                
            elif len(mm) == 1:
                for key in mm:
                    q.append((mm[key], step, l+1))
            else:
                for key in mm: 
                    q.append((mm[key], l+(key!='end'), l+1))

    return ans

def solution(words):
    answer = 0
    words = sorted(words)
    memo = {}
    for word in words:
        current = memo
        for i, w in enumerate(word):
            if current.get(w):
                current = current[w]
            else:
                current[w] = {}
                current = current[w]
                if i == len(word)-1:
                    current['end'] = True
    
    answer = count(memo)
    
    return answer