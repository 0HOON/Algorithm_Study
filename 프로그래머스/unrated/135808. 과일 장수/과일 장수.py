def solution(k, m, score):
    answer = 0
    box = 0
    for s in sorted(score, reverse=True):
        box += 1
        if box == m:
            answer += s * m
            box = 0
    return answer