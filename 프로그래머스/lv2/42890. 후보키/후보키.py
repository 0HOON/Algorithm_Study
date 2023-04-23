from collections import deque

def need_to_check(cols, candidate_keys):
    for k in candidate_keys:
        if k & cols == k:
            return False
    return True

def check(relation, cols):
    columns = []
    i = 0
    while cols > 0:
        if cols & 1:
            columns.append(i)
        i += 1
        cols = cols >> 1
        
    func = lambda x: tuple([x[c] for c in columns])
    tmp = list(map(func, relation))
    return len(tmp) == len(set(tmp))

def solution(relation):
    answer = 0
    N = len(relation[0])
    q = deque([2**i for i in range(N)])
    candidate_keys = []
    while len(q) > 0:
        cols = q.popleft()
        if need_to_check(cols, candidate_keys):
            if check(relation, cols):
                answer += 1
                candidate_keys.append(cols)
            else:
                tmp = 1<<(N-1)
                while not(tmp & cols):
                    q.append(tmp | cols)
                    tmp = tmp >> 1
                    
    return answer