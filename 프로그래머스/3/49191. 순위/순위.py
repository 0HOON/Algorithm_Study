def solution(n, results):
    answer = 0
    memo = [[0]*n for _ in range(n)]
    for a, b in results:
        memo[a-1][b-1] = True
        
    for i in range(n):
        # for m in memo:
        #     print(m)
        # print("***")
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if memo[j][i]:
                    memo[j][k] = memo[j][k] or memo[i][k]
        
    for i in range(n):
        s = 0
        for j in range(n):
            s += memo[j][i]
        if s == n - sum(memo[i])-1:
            answer += 1
    
    return answer