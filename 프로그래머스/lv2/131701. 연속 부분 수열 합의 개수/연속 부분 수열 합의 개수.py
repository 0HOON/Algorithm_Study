def solution(elements):
    max_len = len(elements)
    elements = elements + elements[:-1]
    cumsum = [0]
    for e in elements:
        cumsum.append(cumsum[-1]+e)
    
    ans = []
    for n in range(1, max_len+1):
        i = 0
        while i+n < len(cumsum):
            ans.append(cumsum[i+n]-cumsum[i])
            i += 1
    
    answer = len(set(ans))
    
    return answer