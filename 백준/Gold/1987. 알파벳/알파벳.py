from collections import deque

def PossibleBlock(r, c):
    res = []
    if r > 0:
        res.append((r-1, c))
    if r < R-1:
        res.append((r+1, c))
    if c > 0:
        res.append((r, c-1))
    if c < C-1:
        res.append((r, c+1))
    return res

R, C = list(map(int, input().split()))

board = []
for _ in range(R):
    board.append(list(map(lambda x: 2**(ord(x)-25), list(input()))))

stack = deque([(0, 0, board[0][0],1)])
ans = 0
memo = [[{} for j in range(C)] for _ in range(R)]

while len(stack) > 0:
    r, c, visited, n = stack.pop()
    for i, j in PossibleBlock(r, c):
        if not(visited & board[i][j]):
            v = visited|board[i][j]
            if memo[i][j].get(v, False):
                continue
            else:
                stack.append((i, j, v, n+1))
                memo[i][j][v] = True
        else:
            if ans < n:
                ans = n

print(ans)