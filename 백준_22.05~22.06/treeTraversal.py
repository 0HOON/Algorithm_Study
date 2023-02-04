# 1991 트리 순회 실버1

class node:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return self.value

  def preorder(self):
    l, r = "", ""
    if str(self.left) != '.': l = self.left.preorder()
    if str(self.right) != '.': r = self.right.preorder()
    return self.value + l + r
  
  def inorder(self):
    l, r = "", ""
    if str(self.left) != '.': l = self.left.inorder()
    if str(self.right) != '.': r = self.right.inorder()
    return l + self.value + r

  def postorder(self):
    l, r = "", ""
    if str(self.left) != '.': l = self.left.postorder()
    if str(self.right) != '.': r = self.right.postorder()
    return l + r + self.value


N = int(input())
tmp = []

v, l, r = input().split()
left = node(l, None, None)
right = node(r, None, None)
root = node(v, left, right)
if str(left) != '.': tmp.append(left)
if str(right) != '.': tmp.append(right)

for i in range(N-1):
  v, l, r = input().split()
  new_l = node(l, None, None)
  new_r = node(r, None, None)
  for n in tmp:
    if str(n) == v:
      n.left = new_l
      n.right = new_r
      tmp.remove(n)
      if str(new_l) != '.': tmp.append(new_l)
      if str(new_r) != '.': tmp.append(new_r)
      break
  
print(root.preorder())
print(root.inorder())
print(root.postorder())