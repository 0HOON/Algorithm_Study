def solution(a):
    '''
    왼쪽 중 가장 작은 녀석, 오른쪽 중 가장 작은 녀석 둘 중 하나는 나보다 커야 함.
    '''
    answer = 0
    left_min = [1e9+1]*len(a)
    for i, n in enumerate(a[:-1]):
        left_min[i+1] = min(left_min[i], n)
    
    right_min = 1e9+1
    i = len(a)-1
    while i >= 0:
        if not (right_min < a[i] and left_min[i] < a[i]):
            answer += 1
        right_min = min(right_min, a[i])
        i -= 1
        
    return answer