def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))
    storey = list(reversed([0] + storey))
    for i in range(len(storey)-1):
        n = storey[i]
        if n < 5 or (n == 5 and storey[i+1] <= 4):
            answer += n
        else:
            storey[i + 1] += 1
            answer += 10-n
    answer += storey[-1]
    return answer