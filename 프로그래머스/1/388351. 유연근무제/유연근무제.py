def solution(schedules, timelogs, startday):
    answer = 0
    for s, log in zip(schedules, timelogs):
        target = target_time(s)
        answer += 1
        for i, t in enumerate(log):
            if ((i+startday)%7 != 0) and ((i+startday)%7 != 6) and (t > target):
                answer -= 1
                break
            
    return answer

def target_time(s):
    h = s//100
    m = s%100
    m += 10
    if m >= 60:
        h += 1
        m -= 60
    return h*100 + m