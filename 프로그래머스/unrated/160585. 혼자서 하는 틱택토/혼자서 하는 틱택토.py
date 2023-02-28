def check_3(board):
    line = {'O': 0, 'X': 0}
    for row in board:
        if row[0] != '.' and row[0] == row[1] and row[1] == row[2]:
            line[row[0]] += 1
    
    for col in range(3):
        if board[0][col] != '.' and board[0][col] == board[1][col] and board[0][col] == board[2][col]:
            line[board[0][col]] += 1
    
    if board[0][0] != '.' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        line[board[0][0]] += 1
    
    if board[0][2] != '.' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        line[board[0][2]] += 1
        
    return line
    
def solution(board):
    num = {'O': 0, 'X': 0, '.': 0}
    for row in board:
        for r in row:
            num[r] += 1
    if num['O'] < num['X'] or num['O'] > num['X']+1:
        return 0
    
    line = check_3(board)
    if line['O'] > 2 or line['X'] > 2:
        return 0
    
    if line['O'] > 0 and line['X'] > 0:
        return 0
    
    if line['O'] > 0 and num['O'] != num['X']+1:
        return 0
    
    if line['X'] > 0 and num['O'] != num['X']:
        return 0
    
    return 1