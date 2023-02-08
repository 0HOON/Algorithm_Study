from heapq import heappop, heappush

def solution(n, k, enemy):
    max_i = None
    defenced = []
    for i, e in enumerate(enemy):
        if e > n and k == 0:
            i-=1
            break
        elif e > n and k > 0:
            if len(defenced) == 0 or e > -defenced[0]:
                k -= 1
            else:
                n += -heappop(defenced)-e
                heappush(defenced, -e)
                k -= 1
        elif e <= n:
            heappush(defenced, -e)
            n -= e
        
    return i +1