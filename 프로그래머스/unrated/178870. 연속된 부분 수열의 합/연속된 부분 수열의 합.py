def solution(sequence, k):
    i = 0
    j = 0
    s = sequence[0]
    ans = []
    while i <= j and j < len(sequence):
        if s > k:
            s -= sequence[i]
            i += 1
        elif s < k:
            j += 1
            if j < len(sequence):
                s += sequence[j]
        else:
            ans.append((j-i-1, i, j))
            s -= sequence[i]
            i += 1
            j += 1
            if j < len(sequence):
                s += sequence[j]
                
    answer = sorted(ans)[0][1:]
            
    return answer