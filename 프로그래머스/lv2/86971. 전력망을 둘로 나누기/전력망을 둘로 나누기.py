class node():
    def __init__(self, n):
        self.n = n
        self.children = []
        self.n_children_total = 0
        
    def add_child(self, child):
        self.children.append(child)
        
    def n_children(self):
        return len(self.children)
    
    def calculate_total_children(self):
        self.n_children_total = self.n_children()
        for c in self.children:
            self.n_children_total += c.calculate_total_children()
        
        return self.n_children_total
    
    def min_diff(self, k):
        # k = 내 위에 몇개 있는지
        if self.n_children() == 0:
            return k
        tmp_min = float('inf')
        for c in self.children:
            k_ = k + self.n_children_total - c.n_children_total
            diff = abs(k_ - c.n_children_total - 1)
            tmp_min = min(tmp_min, c.min_diff(k_), diff)
            
        return tmp_min
    
def build_tree(n, nodes, wires):
    for a, b in wires:
        if a == n and nodes[b] == None:
            nodes[b] = node(b)
            nodes[a].add_child(nodes[b])
            
        elif b == n and nodes[a] == None:
            nodes[a] = node(a)
            nodes[b].add_child(nodes[a])
    
    for c in nodes[n].children:
        build_tree(c.n, nodes, wires)
    
def solution(n, wires):
    nodes = [None]*(n+1)
    nodes[1] = node(1)
    build_tree(1, nodes, wires)
        
    nodes[1].calculate_total_children()
    answer = nodes[1].min_diff(0)
        
    return answer