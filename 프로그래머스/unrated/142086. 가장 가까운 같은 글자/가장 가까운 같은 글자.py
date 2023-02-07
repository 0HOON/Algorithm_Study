def solution(s):
    answer = []
    d = {}
    for i, c in enumerate(s):
        if d.get(c) == None:
            answer.append(-1)
            d[c] = i
        else:
            answer.append(i - d[c])
            d[c] = i
    return answer