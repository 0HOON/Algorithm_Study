def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []       
    big = 0 
    for i in range(len(numbers)):
        if len(stack) == 0 or stack[-1][0] >= numbers[i]:
            stack.append((numbers[i], i))
        else:
            for k in range(len(stack)-1 , -1, -1):
                if stack[k][0] >= numbers[i]:
                    break
                else:
                    answer[stack[k][1]] = numbers[i]
                    del stack[k]
                    
            stack.append((numbers[i], i))
    
    return answer