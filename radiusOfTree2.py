class node:
    def __init__(self, i, parent, left, right):
        self.i = i
        self.parent = parent
        self.d_p = 0
        self.left = left
        self.d_l = 0
        self.right = right
        self.d_r = 0

    def get_max_distance(self, f):
        d = 0
        v = self.i
        if self.parent != None and self.parent != f:
            new_d, new_v = tree[self.parent].get_max_distance(self.i)
            new_d += self.d_p
            if d < new_d:
                d = new_d
                v = new_v

        if self.left != None and self.left != f:
            new_d, new_v = tree[self.left].get_max_distance(self.i)
            new_d += self.d_l
            if d < new_d:
                d = new_d
                v = new_v

        if self.right != None and self.right != f:
            new_d, new_v = tree[self.right].get_max_distance(self.i)
            new_d += self.d_l
            if d < new_d:
                d = new_d
                v = new_v  

        return d, v

N = int(input())

tree = [node(i, None, None, None) for i in range(N+1)]
edges = []
for i in range(N-1):
    P, C, E = list(map(int, input().split()))
    if tree[P].left == None:
        tree[P].left = C
        tree[P].d_l = E
        tree[C].parent = P
        tree[C].d_p = E
        continue
    tree[P].right = C
    tree[P].d_r = E
    tree[C].parent = P
    tree[C].d_p = E

d, v = tree[1].get_max_distance(None)
d, v = tree[v].get_max_distance(None)

print(d)