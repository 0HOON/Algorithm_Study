from copy import deepcopy

class Board:
    def __init__(self, board):
        self.board = deepcopy(board)
    
    def flip_row(self, row):
        self.board[row] = [(not r) for r in self.board[row]]
    
    def flip_col(self, col):
        for row in self.board:
            row[col] = not row[col]
            
    def change_to(self, target):
        ans = 0
        
        for i, is_white in enumerate(self.board[0]):
            if target[0][i] != is_white:
                ans += 1
                self.flip_col(i)
        
        for i, row in enumerate(self.board):
            if i == 0:
                continue
            if row != target[i]:
                self.flip_row(i)
                ans += 1
                if self.board[i] != target[i]:
                    return False, 0
            
        return True, ans
    
    def print_board(self):
        print('='*len(self.board))
        for row in self.board:
            print(row)
    
def solution(beginning, target):
    answer = -1
    bf = beginning[0]
    tf = target[0]
    
    b = Board(beginning)
    solved, ans = b.change_to(target)
    
    if solved:
        answer = ans
    
    beginning[0] = [not r for r in beginning[0]]
    b = Board(beginning)
    solved, ans = b.change_to(target)
    
    if solved:
        answer = min(answer, ans+1) if answer > -1 else ans+1
    
    return answer