from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    total_w = 0
    q = deque([0]*bridge_length)
    i = 0
    while True:
        answer += 1
        t = truck_weights[i] if i<len(truck_weights) else 0
        p = q.popleft()
        total_w -= p
        if p == -1:
            break
        if total_w + t <= weight:
            if i == len(truck_weights)-1:
                q.append(-1)
            else:
                q.append(t)
                total_w += t
                i += 1
                
        else:
            q.append(0)
                
    return answer