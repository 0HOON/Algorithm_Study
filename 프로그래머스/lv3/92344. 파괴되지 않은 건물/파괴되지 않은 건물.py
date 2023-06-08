def solve(board, skill):
    seed = [[0]*len(board[0]) for _ in range(len(board))]
    for s in skill:
        t, r1, c1, r2, c2, deg = s
        if t==1: deg = -deg
        
        seed[r1][c1] += deg
        if c2+1 < len(board[0]):
            seed[r1][c2+1] -= deg
        if r2+1 < len(board):
            seed[r2+1][c1] -= deg
            if c2+1 < len(board[0]):
                seed[r2+1][c2+1] += deg
    
    for i in range(len(seed)):
        for j in range(1, len(seed[0])):
            seed[i][j] += seed[i][j-1]
    
    
    for j in range(len(seed[0])):
        for i in range(1, len(seed)):
            seed[i][j] += seed[i-1][j]
    
    ans = 0
    for i in range(len(seed)):
        for j in range(len(seed[0])):
            ans += (seed[i][j] + board[i][j])>0
            
    return ans
            
def solution(board, skill):
    answer = solve(board, skill)
    
    return answer