def solution(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    i = len(B)-1
    for a in A[::-1]:
        if a >= B[i]:
            continue
        else:
            i -= 1
            answer += 1
    return answer