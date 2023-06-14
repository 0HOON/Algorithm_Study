from copy import deepcopy
def solution(triangle):
    answer = 0
    new_triangle = deepcopy(triangle)
    for i in range(len(triangle)-1):
        for j, n in enumerate(new_triangle[i]):
            new_triangle[i+1][j] = max(new_triangle[i+1][j], triangle[i+1][j] + n)
            new_triangle[i+1][j+1] = max(new_triangle[i+1][j+1], triangle[i+1][j+1] + n)
    
    return max(new_triangle[-1])