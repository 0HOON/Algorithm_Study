def add_num(s, num):
  if len(s) == 0:
    return str(num)
  else:
    return s + ' ' + str(num)

def print_nums(nums, s, used, m):
  if sum(used) == m-1:
    for i, u in enumerate(used):
      if not u:
        print(add_num(s, nums[i]))
  
  else:
    for i, u in enumerate(used):
      if not u:
        used[i] = True
        print_nums(nums, add_num(s, nums[i]), used, m)
        used[i] = False

n, m = list(map(int, input().split()))
nums = sorted(list(map(int, input().split())))
used = [False] * n

print_nums(nums, '', used, m)