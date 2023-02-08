def solution(k, tangerine):
    answer = 0
    size = {}
    for t in tangerine:
        size[t] = size.get(t, 0) + 1
    
    sorted_tangerine = sorted(size.items(), key=lambda x: x[1], reverse=True)
    for _, t in sorted_tangerine:
        k -= t
        answer += 1
        if k <= 0:
            break
    return answer