
def get_value(num_item, max_weight, weights, values, memo):
  if num_item <= 0 or max_weight <= 0:
    return 0
  
  if memo.get(num_item, False) and memo[num_item].get(max_weight, False):
    return memo[num_item][max_weight]
     
  a = get_value(num_item-1, max_weight, weights, values, memo)
  if max_weight - weights[num_item-1] >= 0:
    b = get_value(num_item-1, max_weight - weights[num_item-1], weights, values, memo) + values[num_item-1]
  else: b = 0

  memo[num_item][max_weight] = max(a, b)

  return memo[num_item][max_weight]

n, k = list(map(int, input().split()))

weights = []
values = []

for _ in range(n):
  w, v = list(map(int, input().split()))
  weights.append(w)
  values.append(v)

memo = {(i+1): {} for i in range(n)}


print(get_value(n, k, weights, values, memo))