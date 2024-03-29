from collections import deque

def is_fit(uid, bid):
    if len(uid) != len(bid):
        return False
    
    for u, b in zip(uid, bid):
        if u == b or b == '*':
            continue
        else:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    # 각 제재 아이디마다 가능한 아이디 구해놓기
    possible_banned = {}
    for bid in banned_id:
        tmp = []
        for uid in user_id:
            if is_fit(uid, bid):
                tmp.append(uid)
        possible_banned[bid] = tmp
    
    # q에 넣으면서 완전 탐색
    memo = {}
    q = deque([(0, tuple())])
    while len(q) > 0:
        n, key = q.popleft()
        
        if n >= len(banned_id):
            if (memo.get(key) is None):
                memo[key] = 1
                answer += 1
            continue
            
        for p in possible_banned[banned_id[n]]:
            if p not in key:
                q.append((n+1, tuple(sorted(key + (p,)))))
        
    
        
    return answer