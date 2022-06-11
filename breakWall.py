# 2206 벽 부수고 이동하기 골드4
# list 사용시 안되다가 deque 사용하니 성공... list 속도가 아주 느린 것으로 보인다.


from collections import deque

def check(next):
  if wall[next[0]][next[1]] == 1:
    if next[2] == 0:
      if visited[next[0]][next[1]][1] < 0:
        qq.append([next[0], next[1], 1, next[3]])
        visited[next[0]][next[1]][1] = next[3]
  else:
    if visited[next[0]][next[1]][0] < 0:
      if visited[next[0]][next[1]][next[2]] < 0:
        qq.append(next)
        visited[next[0]][next[1]][next[2]] = next[3]

def visit(q):
  #상
  if q[0] > 0:
    next = [q[0] - 1, q[1], q[2], q[3] + 1]
    check(next)
  #하
  if q[0] < N-1:
    next = [q[0] + 1, q[1], q[2], q[3] + 1]
    check(next)
  #좌
  if q[1] > 0:
    next = [q[0], q[1] - 1, q[2], q[3] + 1]
    check(next)
  #우
  if q[1] < M-1:
    next = [q[0], q[1] + 1, q[2], q[3] + 1]
    check(next)

N, M = list(map(int, input().split()))

wall = []
visited = []

for i in range(N):
  wall.append(list(map(int, input())))
  # visited[i][j][0] : 벽 안부수고 방문 , visited[i][j][1] : 벽 부수고 방문
  visited.append([[-1, -1] for j in range(M)])

qq = deque()
qq.append([0, 0, 0, 1])
visited[0][0][0] = 1

while len(qq) > 0:
  visit(qq.popleft())
  if visited[N-1][M-1][0] * visited[N-1][M-1][1] < 0:
    break

print(max(visited[N-1][M-1]))