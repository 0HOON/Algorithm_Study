import heapq
def solution(n, works):
    # max 값 줄이기?
    # max heap
    
    answer = 0
    h = []
    for w in works:
        heapq.heappush(h, -w)
    
    for i in range(n):
        a = heapq.heappop(h)
        if a == 0:
            break
        heapq.heappush(h, a+1)
    
    for w in h:
        answer += w**2
        
    return answer