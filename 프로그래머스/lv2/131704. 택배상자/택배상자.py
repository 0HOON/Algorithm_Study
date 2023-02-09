def solution(order):
    answer = 0
    stack = []
    i = 0
    j = 0
    while j < len(order):
        o = order[j]
        main = i+1
        side = stack[-1] if len(stack)>0 else None
        if main == o:
            answer += 1
            j += 1
            i += 1
            continue
        elif side == o:
            stack.pop()
            answer += 1
            j += 1
            continue
        elif main > o:
            break
        else:
            stack.append(main)
            i += 1
                
    return answer