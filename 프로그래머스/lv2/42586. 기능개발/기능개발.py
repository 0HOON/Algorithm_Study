from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        ans = 0
        while len(progresses) > 0 and progresses[0]>=100:
            progresses.popleft()
            speeds.popleft()
            ans += 1
        if ans > 0:
            answer.append(ans)
    return answer