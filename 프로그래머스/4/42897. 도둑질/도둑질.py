def solution(money):
    answer = 0
    # memo[i][0]: 이 집 훔쳤을 때 최대
    # memo[i][1]: 이 집 훔치지 않았을 때 최대
    memo_include_first = [[0, 0] for _ in range(len(money))]
    memo_include_first[0][0] = money[0]
    memo_exclude_first = [[0, 0] for _ in range(len(money))]
    for i, m in enumerate(money[:-1]):
        if i > 0:
            memo_include_first[i][0] = memo_include_first[i-1][1] + m
            memo_include_first[i][1] = max(
                memo_include_first[i-1][1],
                memo_include_first[i-1][0]
            )
            
            memo_exclude_first[i][0] = memo_exclude_first[i-1][1] + m
            memo_exclude_first[i][1] = max(
                memo_exclude_first[i-1][1],
                memo_exclude_first[i-1][0]
            )
            
    answer = max(
        memo_include_first[i][0],
        memo_include_first[i][1],
        memo_exclude_first[i][0],
        memo_exclude_first[i][1]+money[i+1]
    )
    return answer