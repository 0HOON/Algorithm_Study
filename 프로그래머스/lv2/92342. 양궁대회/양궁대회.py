import copy

def score(arrow_list, value):
    score = 0
    for i, a in enumerate(arrow_list):
        if a > 0:
            score += value[i]
    return score

def MaxScore(i, j, memo, info, value):
    if i == 0 or j==0:
        return [0] * 11
    
    if memo[i][j] != None:
        return copy.deepcopy(memo[i][j])
    
    memo[i][j] = MaxScore(i-1, j, memo, info, value)
    if j > info[i]:
        tmp = MaxScore(i-1, j-info[i]-1, memo, info, value)
        if score(tmp, value)+value[i] > score(memo[i][j], value):
            tmp[i] = info[i]+1
            memo[i][j] = tmp
        elif score(tmp, value)+value[i] == score(memo[i][j], value):
            for a, b in zip(memo[i][j], tmp):
                if a == b:
                    continue
                if b > a:
                    tmp[i] = info[i]+1
                    memo[i][j] = tmp        
                break
        
    return copy.deepcopy(memo[i][j])

def solution(n, info):
    answer = []
    info = info[::-1]
    # memo[i][j]: i점까지 이용, j개 화살로 얻을 수 있는 최대 점수 구성
    memo = [[None for i in range(n+1)] for _ in range(11)]
    value = [2*(i) if a > 0 else i for i, a in enumerate(info)]
    appeach_score = score(info, list(range(11)))
    rian_score = MaxScore(10, n, memo, info, value)
    
    score_diff = score(rian_score, value) - appeach_score
    
    if sum(rian_score) < n:
        rian_score[0] += n-sum(rian_score)
        
    if score_diff <= 0:
        return [-1]
        
    return rian_score[::-1]