import sys

sys.setrecursionlimit(100000)
class Node():
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.parent = None
        self.left = None
        self.right = None

    def trav(self, tree, lv, answer, leftmost, rightmost):
        if lv >= len(tree):
            answer[0].append(self.n)
            answer[1].append(self.n)
            return
        
        answer[0].append(self.n)
        for node in tree[lv]:
            if node.x < self.x and node.x >= leftmost:
                self.left = node
                self.left.parent = self
                self.left.trav(tree, lv+1, answer, leftmost, self.x)
            elif node.x > self.x and node.x <= rightmost:
                self.right = node
                self.right.parent = self
                self.right.trav(tree, lv+1, answer, self.x, rightmost)
        
        answer[1].append(self.n)
        return
        
def solution(nodeinfo):
    answer = [[], []]
    
    nodeinfo = list(zip(nodeinfo, [i+1 for i in range(len(nodeinfo))]))
    tree = []
    last_y = -1
    for (x, y), n in sorted(nodeinfo, key=lambda x: (-x[0][1], x[0][0])):
        new_node = Node(n, x, y)
        if last_y != y:
            last_y = y
            tree.append([])
        tree[-1].append(new_node)
    
    tree[0][0].trav(tree, 1, answer, 0, 100000)
        
    return answer