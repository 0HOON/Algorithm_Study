# 9251 LCS 골드5

A = input()
B = input()

LCS = [0] * len(A)
for ib, b in enumerate(B):
  new_LCS = [0] * len(A)
  for ia, a in enumerate(A):
    if a == b:
      if ia == 0:
        new_LCS[ia] = 1
      else:
        new_LCS[ia]= LCS[ia - 1] + 1
    else:
      new_LCS[ia] = max(LCS[ia], new_LCS[ia-1])
  LCS = new_LCS
  
print(LCS[-1])