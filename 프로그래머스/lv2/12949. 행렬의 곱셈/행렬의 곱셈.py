def solution(arr1, arr2):
    arr2 = [[row[col] for row in arr2] for col in range(len(arr2[0]))]
    answer = [[0]*len(arr2) for _ in range(len(arr1))]
    for r, row in enumerate(arr1):
        for c, col in enumerate(arr2):
            for a, b in zip(row, col):
                answer[r][c] += a*b
    
    return answer