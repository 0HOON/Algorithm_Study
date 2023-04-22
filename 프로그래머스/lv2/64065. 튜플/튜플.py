def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s = list(map(lambda x: [int(n) for n in x.split(',')], s))
    s = sorted(s, key=len)
    used = {x: False for x in s[-1]}
    for ss in s:
        for n in ss:
            if not used[n]:
                answer.append(n)
                used[n] = True
                break
    return answer