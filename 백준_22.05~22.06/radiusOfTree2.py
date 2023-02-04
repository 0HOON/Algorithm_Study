# 1967 트리의 지름 골드4
class node:
    def __init__(self, i):
        self.i = i
        self.parent = None
        self.d = 0
        self.children = []

    def get_max_distance(self, f):
        d = 0
        v = self.i

        if self.parent != None and self.parent != f:
            new_d, new_v = tree[self.parent].get_max_distance(self.i)
            new_d += self.d
            if d < new_d:
                d = new_d
                v = new_v

        for c in self.children:
            if c != f:
                new_d, new_v = tree[c].get_max_distance(self.i)
                if d < new_d:
                    d = new_d
                    v = new_v

        if f == self.parent:
            return d + self.d, v
        
        return d, v

N = int(input())

tree = [node(i) for i in range(N+1)]
edges = []
for i in range(N-1):
    P, C, E = list(map(int, input().split()))
    tree[P].children.append(C)
    tree[C].parent = P
    tree[C].d = E

d, v = tree[1].get_max_distance(None)
d, v = tree[v].get_max_distance(None)

print(d)