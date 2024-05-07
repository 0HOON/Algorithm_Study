from collections import deque

def str2min(s):
    hh, mm = s.split(':')
    return int(hh)*60 + int(mm)

def min2str(m):
    hh, mm = divmod(m, 60)
    return f'{hh:02d}:{mm:02d}'

def solution(n, t, m, timetable):
    line = []
    timetable = sorted([str2min(t) for t in timetable])
    answer = min2str(timetable[0]-1)
    q = deque(timetable)
    time = str2min('09:00')
    for bus in range(n):
        line = []
        if q:
            if q[0] > time:
                answer = min2str(time)
            else:
                answer = min2str(q[0]-1)
        
            
        while q and q[0] <= time and len(line) < m:
            if line and q[0] > line[-1]:
                answer = min2str(q[0]-1)
            line.append(q.popleft())
            
        time += t
        if len(line) < m:
            if bus < n-1:
                answer = min2str(time-1)
            else:
                answer = min2str(time-t)
        
        
    return answer