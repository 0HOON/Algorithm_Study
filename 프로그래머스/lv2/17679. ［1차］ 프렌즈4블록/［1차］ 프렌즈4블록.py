def delete(board):
    deleted = [[False]*len(board[0]) for _ in range(len(board))]
    grid = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            same = True
            block = ''
            for ii, (x, y) in enumerate(grid):
                if ii == 0:
                    block = board[i+x][j+y]
                elif block == '.' or block != board[i+x][j+y]:
                    same = False
                    break
            if same:
                for x, y in grid:
                    deleted[i+x][j+y] = True
    drop(board, deleted)    
    return sum(list(map(sum, deleted)))

def drop(board, deleted):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if deleted[i][j]:
                board[i][j] = '.'
    
    for col in range(len(board[0])):
        new_col = []
        for row in range(len(board)-1, -1, -1):
            if board[row][col] != '.':
                new_col.append(board[row][col])
        new_col = ['.']*(len(board)-len(new_col)) + new_col[::-1]
        for row in range(len(board)):
            board[row][col] = new_col[row]
            
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        ans = delete(board)
        answer += ans
        if ans == 0:
            break
    return answer