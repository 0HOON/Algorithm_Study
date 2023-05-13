def solution(people, limit):
    answer = 0
    people = sorted(people)
    boat = 0
    i = 0
    j = len(people)-1
    while i <= j:
        if i == j:
            answer += 1
            break
            
        if people[i] + people[j] < limit:
            boat = people[i] + people[j]
            while boat <= limit and i <= j:
                i += 1
                boat += people[i]
            j -= 1
            answer += 1
            
        elif people[i] + people[j] == limit:
            i += 1
            j -= 1
            answer += 1
        else:
            j -= 1
            answer += 1
            
    return answer