def is_possible(skill, st):
    memo = {s: i for i, s in enumerate(skill)}
    i = 0
    for s in st:
        if memo.get(s) == None:
            continue
        elif memo.get(s) == i:
            i += 1
        elif memo.get(s) > i:
            return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        answer += is_possible(skill, st)
    
    return answer