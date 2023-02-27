N = int(input())
solution = list(map(int, input().split()))

min_ = (float('inf'), 0, 0)

i = 0
j = N-1
while i < j and min_[0] > 0:
  sum_ = solution[i] + solution[j]
  if abs(sum_) < min_[0]:
    min_ = (abs(sum_), solution[i], solution[j])

  if sum_ < 0:
    i += 1
  else:
    j -= 1
  
print(min_[1], min_[2])