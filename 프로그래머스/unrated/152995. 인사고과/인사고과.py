def solution(scores):
    answer = 0
    sorted_scores = sorted(scores, key=lambda x: x[0], reverse=True)
    # 근무 태도 점수가 key미만일 때 인센티브 받기 위한 최소 동료 평가 점수
    max_scores = {}
    max_scores[sorted_scores[0][0]] = sorted_scores[0][1]
    big = sorted_scores[0][1]
    for a, b in sorted_scores:
        if big < b:
            big = b
            max_scores[a] = b
    
    # 완호 인센티브 받는지 확인
    wanho = scores[0]
    for k, m in sorted(max_scores.items()):
        if wanho[0] < k and wanho[1] < m:
            return -1
        
    incentives = []
    sorted_scores = sorted(scores[1:])
    for k, m in sorted(max_scores.items()):
        for i, s in enumerate(sorted_scores):
            if s[0] < k and s[1] < m:
                # 인센티브 제외
                continue
            elif s[0] >= k:
                # 다음 key 필요
                sorted_scores = sorted_scores[i:]
                break
            elif s[1] >= m:
                # 인센티브 받는 score
                incentives.append(s)
                
    incentives.extend(sorted_scores)
    incentives = list(map(lambda x: x[0] + x[1], incentives))
    # 완호 등수 확인
    wanho = sum(scores[0])
    for i, s in enumerate(sorted(incentives, reverse=True)):
        if wanho >= s:
            return i+1
    
    return len(incentives) + 1