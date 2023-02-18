def solution(cards1, cards2, goal):
    while len(goal) > 0:
        w = goal.pop(0)
        if len(cards1) > 0 and w == cards1[0]:
            cards1.pop(0)
            continue
        elif len(cards2) > 0 and w == cards2[0]:
            cards2.pop(0)
            continue
        else:
            return 'No'
    return 'Yes'