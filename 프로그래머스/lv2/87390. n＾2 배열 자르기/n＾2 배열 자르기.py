def idx_to_num(n, idx):
    row, col = divmod(idx, n)
    if col <= row:
        num = row+1
    else:
        num = col+1
    return num
    
def solution(n, left, right):
    answer = [idx_to_num(n, i) for i in range(left, right+1)]
    return answer