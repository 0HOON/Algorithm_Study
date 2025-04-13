# 1) m을 기준으로 한 번 씩 풀기: 
#    cumsum 구해서 각 m에 따른 좌, 우 쿠키 수 계산 O(n)
#    각 m에 대해서 좌, 우 중 많은쪽 하나씩 빼면서 동일해질 때까지 계산 O(n^2) 
#    n=2000이니 충분.
def solution(cookie):
    if len(cookie) < 2: # 바구니가 하나면 나누기 불가능
        return 0
    
    answer = 0
    cumsum = [cookie[0]]
    for c in cookie[1:]:
        cumsum.append(cumsum[-1]+c)
        
    for m in range(len(cookie)-1):
        l = 0
        r = len(cookie)-1
        
        lsum = cumsum[m]
        rsum = cumsum[r] - lsum
        
        while (l<=m) and (r>m):
            if lsum > rsum:
                lsum -= cookie[l]
                l += 1   
            elif lsum < rsum:
                rsum -= cookie[r]                
                r -= 1
            else:
                answer = max(answer, lsum)
                break
                
    return answer