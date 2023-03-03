def check_cycle(s, g, group, hope):
  tmp = []
  tmp_g = g
  while True:
    tmp.append(s)
    group[s] = g
    if s == hope[s]:    # 나 자신. 혼자하기.
      tmp_g = -1
      group[s] = 1
      tmp.pop()
      break
    else:               # 다른 사람 선택
      gh = group[hope[s]]
      if gh == g:      # 다음 사람이 이미 지금 그룹에 속한 경우 = cycle
        break
      elif gh == 1:
        tmp_g = -1     # 다음 사람이 혼자 그룹인경우
        break
      elif gh != 0:    # 다음 사람이 이미 다른 group 속하거나 group 실패
        tmp_g = -1
        break
      else:          # 다음 사람 아직 체크 안함
        s = hope[s]
        continue
      
  if tmp_g != g:
    for t in tmp:
      group[t] = tmp_g
    return g
  else:
    for t in tmp:
      if t == hope[s]:
        break
      group[t] = -1

    return g + 1

N = int(input())
answers = []
for _ in range(N):
  n = int(input())
  hope = list(map(lambda x: int(x)-1, input().split()))
  group = [0] * n     # 0: not checked, 1: self_grouped, -1: not cycle, else: grouped
  g = 2
  for s in range(n):
    if group[s] == 0:
      g = check_cycle(s, g, group, hope)

  ans = 0
  for g in group:
    if g == -1:
      ans += 1
  answers.append(ans)

for ans in answers:
  print(ans)