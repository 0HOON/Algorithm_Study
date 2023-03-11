def check_(survey, choice, score):
    choice = choice - 4
    type_ = survey[choice > 0]
    score[type_] += abs(choice)

def solution(survey, choices):
    answer = ''
    type_ = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = {t: 0 for t in type_}
    for i, s in enumerate(survey):
        check_(s, choices[i], score)
    
    for i in range(4):
        a = type_[2*i]
        b = type_[2*i + 1]
        if score[a] >= score[b]:
            answer += a
        else:
            answer += b
        
    return answer