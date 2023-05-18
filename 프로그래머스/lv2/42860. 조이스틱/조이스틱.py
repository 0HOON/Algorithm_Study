from collections import deque

def solution(name):
    name = list(name)
    tmp = ['A'] * len(name)
    i = 0
    answer = 0
    next_r = 0
    next_l = 0
    
    q = deque([(tuple(tmp), 0, 0)])
    min_n = 99999999
    
    while len(q) > 0:
        tmp_name, i, n = q.popleft()
        tmp_name = list(tmp_name)
        tmp_name[i] = name[i]
        if ''.join(tmp_name) == ''.join(name):
            if n < min_n:
                min_n = n
        else:
            next_r = 0
            next_l = 0
            for r in range(1, len(name)):
                idx = (r+i)%len(name)
                if tmp_name[idx] != name[idx]:
                    next_r = r
                    break
                else:
                    r += 1

            for l in range(1, len(name)):
                idx = i-l
                if idx < 0:
                    idx += len(name)
                if tmp_name[idx] != name[idx]:
                    next_l = l
                    break
                else:
                    l += 1
            idx = (i+next_r)%len(name)
            q.append((tuple(tmp_name), idx, n+next_r))
            idx = i-next_l
            if idx < 0:
                idx += len(name)
            q.append((tuple(tmp_name), idx, n+next_l))
                
    answer = min_n
    
    for c in name:
        tmp = abs(ord(c)-ord('A'))
        tmp = min(tmp, 26-tmp)
        answer += tmp
    return answer