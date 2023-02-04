# 2263 트리의 순회 골드2

import sys
sys.setrecursionlimit(10**6) 

def toPreOrder(in_s, in_e, post_s, post_e):
  if in_s == in_e:
    return str(inorder[in_s]) + " "

  in_root = pos[postorder[post_e]]
  ii = in_root - in_s
  l = ""
  r = ""
  if ii > 0:
    l = toPreOrder(in_s, in_root - 1, post_s, post_s + ii - 1)
  
  if ii < in_e - in_s:
    r = toPreOrder(in_root + 1, in_e, post_s + ii, post_e - 1)
    
  preorder = str(postorder[post_e]) + " " + l + r
  return preorder

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 매번 변수 찾기 for문 돌리는 것 방지
pos=[0]*(N + 1)

for i in range(N):
    pos[inorder[i]]=i

print(toPreOrder(0, N - 1, 0, N - 1)[:-1])