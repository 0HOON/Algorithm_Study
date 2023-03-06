def solution(A, B):
    answer = -1
    for i in range(len(A)):
        tmp = A[-i:] + A[:-i] 
        if tmp == B:
            answer = i
            break
    
    return answer