from heapq import heappush, heappop
from collections import deque
from copy import deepcopy

def wait_time(k, n_mentor, reqs):
    if len(reqs[k]) <= 0:
        return 0
    
    if n_mentor == 0:
        return 999999999
    
    hq = []
    total_wait_time = 0
    for a, b in reqs[k]:
        if len(hq) < n_mentor:
            heappush(hq, a+b)
        else:
            end_time = heappop(hq)
            next_start_time = a
            if end_time > a:
                total_wait_time += end_time-a
                next_start_time = end_time
            heappush(hq, next_start_time + b)
    return total_wait_time

def solution(k, n, reqs):
    req_list = [[] for _ in range(k+1)]
    for a, b, i in reqs:
        req_list[i].append((a, b))
    
    costs = [[0] * (n+1) for _ in range(k+1)]
    wt = 0
    for i in range(1, k+1):
        for j in range(1, n-k+2):
            costs[i][j] = wait_time(i, j, req_list)
            if j == 1:
                wt += costs[i][j]
                
    n_mentors = [1] * (k+1)
    n_mentors[0] = 0
    
    q = deque([(n_mentors, wt)])
    answer = 999999999
    memo = {}
    while len(q) > 0:
        n_mentors, wt = q.popleft()
        if sum(n_mentors) >= n:
            print(n_mentors, wt)
            if answer >= wt:
                answer = wt
        else:
            for i in range(1, k+1):
                tmp = wt - costs[i][n_mentors[i]] + costs[i][n_mentors[i]+1]
                tmp_n_mentors = deepcopy(n_mentors)
                tmp_n_mentors[i] += 1
                if memo.get(tuple(tmp_n_mentors)) is None:
                    memo[tuple(tmp_n_mentors)] = tmp
                    q.append((tmp_n_mentors, tmp))
        
    return answer