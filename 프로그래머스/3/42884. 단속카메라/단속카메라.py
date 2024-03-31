def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    last_cam = -float('inf')
    for s, e in routes:
        if last_cam < s:
            last_cam = e
            answer += 1
        
    return answer