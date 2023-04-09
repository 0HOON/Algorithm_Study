from collections import deque

def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for p in problems:
        if max_alp < p[0]:
            max_alp = p[0]
        if max_cop < p[1]:
            max_cop = p[1]
    
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    
    problems = sorted(
                problems,
                key=lambda x: (min(x[2], max_alp-alp)+min(x[3], max_cop-cop)) / x[4],
                reverse=True
            )
    
    memo = [[float('inf')]*(max_cop+1) for _ in range(max_alp+1)]
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    q = deque([(alp, cop, 0)])
    while len(q) > 0:
        alp_, cop_, t_ = q.popleft()
        if memo[alp_][cop_] <= t_:
            continue
            
        memo[alp_][cop_] = t_
        
        if alp_ >= max_alp and cop_ >= max_cop: # 종료 조건
            continue
        else:
            for p in problems:
                if alp_ >= p[0] and cop_ >= p[1]: # 풀 수 있고
                    tmp_alp = min(max_alp, alp_+p[2])
                    tmp_cop = min(max_cop, cop_+p[3])
                    tmp_t = t_+p[4]
                    if memo[tmp_alp][tmp_cop] > tmp_t: # 푼 결과 상태에 기존 방법보다 빠르게 도달한다면 푼다
                        q.append((tmp_alp, tmp_cop, tmp_t))
                            
    answer = memo[max_alp][max_cop]
    
    return answer