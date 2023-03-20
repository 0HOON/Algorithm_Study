def GetMinDistance(m, n, startX, startY, ballX, ballY):
    dist = []
    if startY != ballY:
        x = [] 
        if startX > 0 and ballX > 0:
            x.append(startX + ballX)
        if startX < m and ballX < m:
            x.append(2*m - startX - ballX)
        if len(x) == 0: # 0에 하나, m에 하나
            x.append(3*m)
        d = (min(x))**2 + (ballY-startY)**2
        dist.append(d)
        
    else:
        if startX < ballX:
            d = (startX + ballX)**2
        else:
            d = (2*m - ballX - startX)**2
        dist.append(d)
        
    if startX != ballX:
        y = []
        if startY > 0 and ballY > 0:
            y.append(startY + ballY)
        if startY < n and ballY < n:
            y.append(2*n - startY - ballY)
        if len(y) == 0:
            y.append(3*n)
        
        d = (min(y))**2 + (ballX-startX)**2
        dist.append(d)
    else:
        if startY < ballY:
            d = (startY + ballY)**2
        else:
            d = (2*n - ballY - startY)**2
        dist.append(d)
        
    return min(dist)

def solution(m, n, startX, startY, balls):
    answer = [GetMinDistance(m, n, startX, startY, x, y) for x, y in balls]
    return answer