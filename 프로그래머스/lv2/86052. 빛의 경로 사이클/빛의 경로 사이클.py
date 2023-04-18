def step(i, j, direction, grid, dir):
    n_row = len(grid)
    n_col = len(grid[0])
    if grid[i][j] == 'S':
        pass
    elif grid[i][j] == 'L':
        direction = (direction-1)%4
    elif grid[i][j] == 'R':
        direction = (direction+1)%4
        
    i = (i + dir[direction][0])%n_row
    j = (j + dir[direction][1])%n_col
    
    return i, j, direction

def solution(grid):
    answer = []
    n_row = len(grid)
    n_col = len(grid[0])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # u, r, d, l 순으로 방향 저장.
    visited = [[[False]*4 for c in range(n_col)] for r in range(n_row)]
    n_visited = 0
    for r in range(n_row):
        for c in range(n_col):
            for d in range(4):
                if not visited[r][c][d]:
                    i = r
                    j = c
                    cycle_len = 0
                    while not visited[i][j][d]:
                        visited[i][j][d] = True
                        i, j, d = step(i, j, d, grid, dir)
                        cycle_len += 1
                    answer.append(cycle_len)
    return sorted(answer)