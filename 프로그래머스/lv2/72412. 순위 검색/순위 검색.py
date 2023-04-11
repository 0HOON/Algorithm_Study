def BinSearch(l, num):
    if num <= l[0]:
        return 0
    if num > l[-1]:
        return len(l)
    
    left = 0
    right = len(l)-1
    
    while left < right:
        mid = (left+right)//2
        mid_n = l[mid]
        if mid_n == num:
            while l[mid] == num:
                mid -= 1
            return mid+1
        elif mid_n < num:
            left = mid+1
        elif mid_n > num:
            right = mid
    # num이 l에서 right번째 원소보다 작거나 같음.            
    return right
            
    
def solution(info, query):
    # cpp, java, python
    # backend, frontend
    # junior, senior
    # chicken, pizza
    m = {
        'cpp': 0,
        'java': 1,
        'python': 2,
        'backend': 0,
        'frontend': 1,
        'junior': 0,
        'senior': 1,
        'chicken': 0,
        'pizza': 1,
    }
    l = [0, 1, 2]
    j = [0, 1]
    c = [0, 1]
    s = [0, 1]
    memo = {(ll, jj, cc, ss):[] for ll in l for jj in j for cc in c for ss in s}
    
    info = sorted(info, key=lambda x: int(x.split()[-1]))
    for i in info:
        l, j, c, s, score = i.split()
        memo[(m[l], m[j], m[c], m[s])].append(int(score))
    
    answer = []
    for q in query:
        l, j, c, s_score = q.split(' and ')
        s, score = s_score.split()
        idx = []
        l = [0, 1, 2] if l == '-' else [m[l]]
        j = [0, 1] if j == '-' else [m[j]]
        c = [0, 1] if c == '-' else [m[c]]
        s = [0, 1] if s == '-' else [m[s]]
        score = int(score)
        for ll in l:
            for jj in j:
                for cc in c:
                    for ss in s:
                        idx.append((ll, jj, cc, ss))
        ans = 0
        for i in idx:
            l = memo[i]
            if len(l) > 0:
                ans += len(l) - BinSearch(l, score)
        answer.append(ans)
    
    return answer