def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    
    for i, c in enumerate(citations):
        if c < i+1:
            return i
    
    return i+1
