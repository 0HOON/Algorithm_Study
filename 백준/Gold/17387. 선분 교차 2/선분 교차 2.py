from math import pi

def IsCrossing(l1, l2):
  x1, y1, x2, y2 = l1
  x3, y3, x4, y4 = l2
  if (min(x1, x2) > max(x3, x4) or 
      min(x3, x4) > max(x1, x2) or
      min(y1, y2) > max(y3, y4) or
      min(y3, y4) > max(y1, y2) ):
      return 0
  if x4 != x3:
    tmp1 = (y4-y3)/(x4-x3) * (x1-x3) + y3 - y1
    tmp2 = (y4-y3)/(x4-x3) * (x2-x3) + y3 - y2
  else:
    tmp1 = x1 - x3
    tmp2 = x2 - x3
  if x1 != x2:
    tmp3 = (y2-y1)/(x2-x1) * (x3-x1) + y1 - y3
    tmp4 = (y2-y1)/(x2-x1) * (x4-x1) + y1 - y4
  else:
    tmp3 = x3 - x1
    tmp4 = x4 - x1
  if abs(tmp1) < 0.00001:
    tmp1 = 0
  if abs(tmp2) < 0.00001:
    tmp2 = 0
  if abs(tmp3) < 0.00001:
    tmp3 = 0
  if abs(tmp4) < 0.00001:
    tmp4 = 0
  tmp = ((tmp1 * tmp2) <= 0) and ((tmp3 * tmp4) <= 0)

  return int(tmp)
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(IsCrossing(l1, l2))