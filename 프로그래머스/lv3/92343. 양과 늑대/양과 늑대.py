class Node:
    def __init__(self, w, l, r):
        self.w = w
        self.l = l
        self.r = r

from collections import deque
from copy import deepcopy

def solution(info, edges):
    Tree = [Node(w, None, None) for w in info]
    for p, c in edges:
        if Tree[p].l == None:
            Tree[p].l = Tree[c]
        else:
            Tree[p].r = Tree[c]
    
    answer = 0
    candidate = []
    if Tree[0].l != None: candidate.append(Tree[0].l)
    if Tree[0].r != None: candidate.append(Tree[0].r)
    
    q = deque([(1, 0, candidate)]) # sheep, wolf, candidate
    while len(q) > 0:
        sheep, wolf, candidate = q.popleft()
        if sheep > answer:
            answer = sheep
        if len(candidate) <= 0:
            continue
        for i, n in enumerate(candidate):
            if sheep > n.w + wolf:
                new_candidate = deepcopy(candidate)
                if n.l != None: new_candidate.append(n.l)
                if n.r != None: new_candidate.append(n.r)
                del new_candidate[i]
                q.append((sheep + (not n.w), wolf + n.w, new_candidate))
    
    return answer