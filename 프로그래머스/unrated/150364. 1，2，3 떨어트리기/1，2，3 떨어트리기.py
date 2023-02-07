# 부모 노드에 숫자 n개 오면
# 자식 노드에 순서대로 숫자 분배
# 리프까지 반복

# 자식노드 분배할 숫자 각각 a, b, c, d...이면
# 부모 노드에서 분배 가능한지 판단, 최대, 최소 횟수 계산, 가능하면 부모 노드가 분배할 숫자 a+b+c+...
# 루트까지 반복.

# 5: (2, 5), 3: (1, 3),      4:(2, 4), 6:(2, 6), 7:(3, 7)
# -> (3, 7)                     ->(9, 12)
# 이런식으로 판단
# 루트노드에서 min 선택 -> 역순으로 분배 -> 리프노드당 횟수 나옴 -> 사전순 작은거 결과로.

def find_min_max(edges_dict, target, node):
    if edges_dict.get(node) == None:
        # leaf 이면
        t = target[node-1]
        m = (t // 3) + ((t % 3) > 0)
        return (True, m, t)
    
    min_list = []
    max_list = []
    children = edges_dict[node]
    for child in children:
        possible, a, b = find_min_max(edges_dict, target, child)
        if not possible:
            return (False, 0, 0)
    
        min_list.append(a)
        max_list.append(b)
    
    # possible 확인
    # 마지막 노드 최소 보다 최대가 작은 놈 있으면
    # or 마지막 노드 최대 + 1 보다 최소가 큰 놈 있으면
    # 
    if min_list[-1] > min(max_list) or max(min_list) > max_list[-1]+1:
        return (False, 0, 0)
    
    tmp = max(min_list)
    idx = len(min_list) - list(reversed(min_list)).index(tmp)
    m = (tmp-1) * len(children) + idx
    
    tmp = min(max_list)
    M = tmp * len(children) + max_list.index(tmp)
    
    return (True, m, M)

def make_answer(edges_dict, target, node, n):
    if edges_dict.get(node) == None:
        # leaf
        t = target[node-1]
        s = n
        three = 0
        two = 0
        one = n
        
        while s < t:
            three += 1
            one -= 1
            s = three * 3 + one
            
        if s > t:
            three -= 1
            two += 1
            
        return [1]*one + [2]*two + [3]*three
    
    ans = []
    children = edges_dict[node]
    for i, child in enumerate(children):
        n_child = n // len(children) + (i < (n % len(children)))
        ans.append(make_answer(edges_dict, target, child, n_child))
    
    answer = []
    for i in range(len(ans[-1])):
        for j in range(len(ans)):
            answer.append(ans[j][i])
    
    for i in range(n % len(children)):
        answer.append(ans[i][-1])
        
    return answer
        
def solution(edges, target):
    answer = []
    edges = sorted(edges, key=lambda x: x[0])
    edges_dict = {}
    for p, c in edges:
        edges_dict[p] = edges_dict.get(p, []) + [c]
    
    for k in edges_dict:
        edges_dict[k] = sorted(edges_dict[k])
        
    possible, m, M = find_min_max(edges_dict, target, 1)
    if not possible:
        return [-1]
    
    answer = make_answer(edges_dict, target, 1, m)
    
    return answer