from heapq import heappush, heappop

def delete_max(q_max, memo):
    while len(q_max) > 0:
        tmp = -heappop(q_max)
        if memo[tmp] >= 1:
            memo[tmp] -= 1
            return tmp
    return None

def delete_min(q_min, memo):
    while len(q_min) > 0:
        tmp = heappop(q_min)
        if memo[tmp] >= 1:
            memo[tmp] -= 1
            return tmp
    return None

def insert_n(n, q_max, q_min, memo):
    heappush(q_min, n)
    heappush(q_max, -n)
    memo[n] = memo.get(n, 0) + 1

def get_answer(q_max, memo):
    ans = []
    while len(q_max) > 0:
        tmp = delete_max(q_max, memo)
        if tmp is not None:
            ans.append(tmp)
    if len(ans) > 0:
        return [ans[0], ans[-1]]
    else:
        return [0, 0]
        
def solution(operations):
    q_max = []
    q_min = []
    memo = {}
    for operation in operations:
        op, n = operation.split()
        if op == 'I':
            insert_n(int(n), q_max, q_min, memo)
        elif n == '1':
            delete_max(q_max, memo)
        else:
            delete_min(q_min, memo)
    
    return get_answer(q_max, memo)