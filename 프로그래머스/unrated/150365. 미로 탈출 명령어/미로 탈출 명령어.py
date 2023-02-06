# 순서: d l r u
# path = [d, l, r, u]
# 횟수 남으면 n - max(x, r) 만큼 du 추가 가능
# 아니면 rl 추가
def find_path(x, y, r, c):
    path = [0, 0, 0, 0]
    n_ud = r - x
    n_rl = c - y
    if n_ud > 0:
        path[0] = n_ud
    else:
        path[3] = -n_ud
    
    if n_rl > 0:
        path[2] = n_rl
    else:
        path[1] = -n_rl
        
    return path

def make_min_path(path, n, m, x, y):
    min_path = ''
    min_path += 'd' * path[0]
    
    n_l = min(y-1, path[1])
    min_path += 'l' * n_l
    path[1] -= n_l
    
    n_rl = min(path[1], path[2])
    min_path += 'rl' * n_rl
    path[2] -= n_rl
    
    min_path += 'r' * path[2]
    min_path += 'u' * path[3]
    
    return min_path

def is_possible(path, k):
    return k >= sum(path) and (k-sum(path)) % 2 == 0

def add_extra(path, n, x, r, k):
    n_extra = int((k-sum(path)) / 2)
    n_ud = min(n - max(x, r), n_extra)
    n_rl = n_extra - n_ud
    path[0] += n_ud
    path[3] += n_ud
    path[1] += n_rl
    path[2] += n_rl
    
def solution(n, m, x, y, r, c, k):
    path = find_path(x, y, r, c)
    if not is_possible(path, k):
        return 'impossible'
    if k > sum(path):
        add_extra(path, n, x, r, k)
    answer = make_min_path(path, n, m, x, y)
    
    return answer