from itertools import combinations

def LSS(str1, str2):
    i = 0
    j = 0
    res = []
    while i < len(str1) and j < len(str2):
        a = str1[i]
        b = str2[j]
        if a < b:
            i += 1
        elif a > b:
            j += 1
        elif a == b:
            res.append(a)
            i += 1
            j += 1
    return tuple(res)

def solution(orders, course):
    answer = []
    menu = []
    orders = [sorted(o) for o in orders]
    for a, b in combinations(orders, 2):
        lss = LSS(a, b)
        if len(lss) > 1:
            menu.append(lss)
    
    course_menu = {}
    for c in course:
        for m in menu:
            if len(m) >= c:
                for cor in combinations(m, c):
                    cor = ''.join(cor)
                    course_menu[cor] = course_menu.get(cor, 0) + 1
    
    for c in course:
        max_n = 0
        ans = []
        for cm, num in course_menu.items():
            if len(cm) == c:
                if max_n < num:
                    ans = [cm]
                    max_n = num
                elif max_n == num:
                    ans.append(cm)
        answer.extend(ans)
    answer = sorted(answer)
    return answer