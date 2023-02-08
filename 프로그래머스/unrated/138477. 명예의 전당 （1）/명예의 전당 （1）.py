def solution(k, score):
    answer = [score[0]]
    sorted_score = [score[0]]
    for s in score[1:]:
        for i, ss in enumerate(sorted_score):
            if ss <= s:
                i -= 1
                break
        sorted_score.insert(i+1, s)
        answer.append(sorted_score[min(k-1, len(sorted_score)-1)])
    return answer