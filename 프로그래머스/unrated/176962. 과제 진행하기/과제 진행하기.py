def t2m(t):
    h, m = list(map(int,t.split(':')))
    return h*60 + m

def DoInStack(t, stack, answer):
    while t > 0 and len(stack) > 0:
        n, left_time = stack.pop(-1)
        if left_time <= t:
            t -= left_time
            answer.append(n)
        else:
            stack.append((n, left_time-t))
            t = 0

def solution(plans):
    # plan = [name, start, time]
    # stack : 남은거 (name, left time)
    plans = [(n, t2m(s), int(t)) for n, s, t in plans]
    plans = sorted(plans, key=lambda x: x[1])
    
    t = plans[0][1]
    stack = []
    answer = []
    for i, p in enumerate(plans):
        if i == len(plans)-1:
            t += p[2]
            answer.append(p[0])
            DoInStack(1000000, stack, answer)
        else:
            next_start_time = plans[i+1][1]
            if t + p[2] <= next_start_time:
                t += p[2]
                answer.append(p[0])
                DoInStack(next_start_time-t, stack, answer)
                t = next_start_time
            else:
                left_time = t+p[2] - next_start_time
                stack.append((p[0], left_time))
                t = next_start_time
                
    return answer