def solution(targets):
    answer = 0
    targets = sorted(targets)
    intercepted = [False]*len(targets)
    for i, (s, e) in enumerate(targets):
        if intercepted[i]:
            continue
        intercepted[i] = True
        idx = i+1
        end = e
        while idx < len(targets) and targets[idx][0] < end:
            intercepted[idx] = True
            end = min(end, targets[idx][1])
            idx += 1
        answer += 1
            
    return answer