from heapq import heappush, heappop
def solution(scoville, K):
    answer = 0
    h = []
    for s in scoville:
        heappush(h, s)
    
    while h[0] < K:
        if len(h) < 2:
            return -1
        a = heappop(h)
        b = heappop(h)
        heappush(h, a+b*2)
        answer += 1
    return answer