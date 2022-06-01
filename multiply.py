# 1629 곱셈 실버 1

def get_mod(A, B, C):
  if B == 1:
    return A

  if B%2 == 1:
    return ((get_mod(A, (B-1)/2, C)**2)%C * A)%C
  
  return (get_mod(A, B/2, C)**2)%C

A, B, C = list(map(int, input().split()))

print(get_mod(A%C, B, C))