N = int(input())
solution = sorted(list(map(int, input().split())))

min_ = (float('inf'), 0, 0)
for idx, k in enumerate(solution):
  i = 0 if idx != 0 else 1
  j = N-1 if idx != N-1 else N-2
  while i < j and min_[0] > 0:
    sum_ = solution[i] + solution[j] + k
    if abs(sum_) < min_[0]:
      min_ = (abs(sum_), solution[i], solution[j], k)

    if sum_ < 0:
      i += 1
      if i == idx:
        i += 1
    else:
      j -= 1
      if j == idx:
        j -= 1

  if min_[0] == 0:
    break

print(*sorted(min_[1:]))