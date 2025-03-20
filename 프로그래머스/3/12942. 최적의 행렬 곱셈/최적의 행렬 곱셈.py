def solution(matrix_sizes):
    memo = {}
    
    answer = rec(0, len(matrix_sizes)-1, memo, matrix_sizes)
            
    return answer

def rec(a, b, memo, matrix_sizes):
    if a + 1 == b:
        return matrix_sizes[a][0] * matrix_sizes[a][1] * matrix_sizes[b][1]
    
    if memo.get((a, b)):
        return memo[(a, b)]
    
    min_val = min(
        rec(a, b-1, memo, matrix_sizes) + matrix_sizes[a][0] * matrix_sizes[b][0] * matrix_sizes[b][1],
        rec(a+1, b, memo, matrix_sizes) + matrix_sizes[a][0] * matrix_sizes[a][1] * matrix_sizes[b][1],
    )
    
    for i in range(a+1, b-1):
        min_val = min(min_val, 
                      rec(a, i, memo, matrix_sizes) + rec(i+1, b, memo, matrix_sizes) + matrix_sizes[a][0] * matrix_sizes[i][1] * matrix_sizes[b][1],
                     )
        
    memo[(a, b)] = min_val
    return memo[(a, b)]
    