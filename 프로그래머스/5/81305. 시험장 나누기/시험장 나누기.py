import sys

def solution(k, num, links):
    '''
    경우의 수가 너무 많다. 10000C5000.
    이런 경우 binary search로 O(log) 풀이가 필요하다.
    '''
    sys.setrecursionlimit(10**6)
    answer = 0
    
    nodes = [node(n, k) for n in num]
    for p, (l, r) in enumerate(links):
        if l > -1:
            nodes[p].l = nodes[l]
            nodes[l].p = nodes[p]
        if r > -1:
            nodes[p].r = nodes[r]
            nodes[r].p = nodes[p]
    
    root = nodes[0]
    while root.p is not None:
        root = root.p
        
    # binary search
    r = 1e4*1e4
    l = 0
    while l < r-1:
        m = (l+r)//2
        s, cut = root.check(m)
        if cut >= k or s > m: #fail
            l = m
        else: #success
            r = m
    return r


class node:
    def __init__(self, n, k):
        self.n = n
        self.l = None
        self.r = None
        self.p = None
        self.k = k
        

    def check(self, n):
        '''
        return (left subtree 합 + right subtree 합 + 지금 값), (left에서 자른 횟수 + right에서 자른 횟수 + 지금 자른 횟수) .
        너무 커지면 자르기.
        k 번 이내로 자르면서 가장 큰 chunk 합이 n 이하가 되도록 할 수 있는지 체크
        '''
        if self.l:
            l_sum, l_cut = self.l.check(n)
        else:
            l_sum, l_cut = 0, 0
            
        if self.r:
            r_sum, r_cut = self.r.check(n)
        else:
            r_sum, r_cut = 0, 0
        
        chunks = sorted([l_sum, r_sum])
        cur_sum = self.n + l_sum + r_sum
        cur_cut = l_cut + r_cut
        
        if cur_cut >= self.k or l_sum > n or r_sum > n or self.n > n:
            return cur_sum, cur_cut
        
        while cur_sum > n and len(chunks) > 0:
            cur_sum -= chunks.pop()
            cur_cut += 1
            
        return cur_sum, cur_cut
            
        
    