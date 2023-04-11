from copy import deepcopy as dc

def PossibleStep(board, r, c):
    res = []
    if r > 0 and board[r-1][c]:
        res.append((r-1, c))
    if r < len(board)-1 and board[r+1][c]:
        res.append((r+1, c))
    if c > 0 and board[r][c-1]:
        res.append((r, c-1))
    if c < len(board[0])-1 and board[r][c+1]:
        res.append((r, c+1))
    return res

def BestMove(board, aloc, bloc, a=True):
    player = aloc if a else bloc
    canwin = False 
    ans = -1
    if board[player[0]][player[1]] == 0:
        return True, 0
    tmp_b = dc(board)
    tmp_b[player[0]][player[1]] = 0
    
    ps = PossibleStep(tmp_b, *player)
    
    if len(ps) < 1:
        return True, 0
    
    for r, c in ps:
        if a:
            cw, n = BestMove(tmp_b, (r, c), bloc, not a)
        else:
            cw, n = BestMove(tmp_b, aloc, (r, c), not a)
            
        if cw: # 하나라도 (무조건)이기는 미래가 보이면 그 중 가장 짧은 횟수 움직임.
            if canwin:
                ans = min(ans, n)
            else:
                canwin = True
                ans = n  
        elif not canwin: # 무조건 지는 미래
            ans = max(ans, n) # 가장 오래 버틸 수 있는 움직임.
            
    return not canwin, ans+1

def solution(board, aloc, bloc):
    _, answer = BestMove(board, aloc, bloc, True)
    
    return answer