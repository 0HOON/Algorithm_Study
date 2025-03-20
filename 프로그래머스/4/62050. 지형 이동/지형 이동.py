from heapq import heappush, heappop

def solution(land, height):
    answer = 0
    n = len(land)
    visited = [[False]*n for _ in range(n)]
    st = [(0, 0)]
    possible_next = []
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while len(st) > 0:
        r, c = st.pop()
        visited[r][c] = True
        for dr, dc in directions:
            rr = r + dr
            cc = c + dc
            if 0 <= rr and rr < n and 0 <= cc and cc < n and not visited[rr][cc]:
                dist = abs(land[rr][cc] - land[r][c])
                if dist <= height:
                    st.append((rr, cc))
                else:
                    heappush(possible_next, (dist, rr, cc))
        
        if len(st) == 0:
            if len(possible_next) > 0:
                while len(possible_next) > 0:
                    d, r, c = heappop(possible_next)
                    if not visited[r][c]:
                        st.append((r, c))
                        answer += d
                        break
                
    return answer