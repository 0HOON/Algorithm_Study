class Node():
    def __init__(self, sales):
        self.children = []
        self.val = [float('inf'), float('inf')]
        self.sales = sales
        self.solved = False
        
    def solve(self):
        if not self.children:
            self.solved = True
            return
        
        val_go = 0
        val_stay = []
        total_val_stay = 0
        need_more = True
        min_sales = float('inf')
        
        for child in self.children:
            if not child.solved:
                child.solve()
                
            if child.children:
                tmp = min(child.val)
                val_go += tmp
                val_stay.append(child.val[0] - tmp)
                    
            else:
                val_stay.append(child.sales)
                
        self.val[0] = val_go + self.sales
        self.val[1] = min(val_stay) + val_go
        
        self.solved = True
        
def solution(sales, links):
    answer = 0
    nodes = []
    for s in sales:
        nodes.append(Node(s))
    for a, b in links:
        nodes[a-1].children.append(nodes[b-1])
    
    nodes[0].solve()
    answer = min(nodes[0].val)
    return answer