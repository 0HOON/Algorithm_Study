n, m = list(map(int, input().split()))
stack = [1]

while True:
  if len(stack) < m:
      stack.append(stack[-1]+1)

  else:
    print(*stack)

    while len(stack) > 0 and stack[-1] == n-m+len(stack):
      stack.pop()

    if len(stack) == 0:
      break

    stack.append(stack.pop()+1)