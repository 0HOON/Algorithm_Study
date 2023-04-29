def solution(s):
    s = list(map(int, s.split()))
    answer = ' '.join([str(min(s)), str(max(s))])
    return answer