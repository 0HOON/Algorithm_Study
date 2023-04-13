def solution(cards):
    answer = 0
    group = [0]
    visited = [False] * len(cards)
    cards = [x-1 for x in cards]
    for n in cards:
        if visited[n]:
            continue
        else:
            visited[n] = True
            group.append(1)
            while True:
                n = cards[n]
                if visited[n]:
                    break
                else:
                    group[-1] += 1
                    visited[n] = True
    group = sorted(group, reverse=True)
    answer = group[0] * group[1]
    return answer