def triangle(size, n):
    if size == 1:
        return [[n]]
    elif size == 2:
        return [[n], [n+1, n+2]]
    elif size == 3:
        return [[n], [n+1, n+5], [n+2, n+3, n+4]]
    else:
        tmp = triangle(size-3, n+(size-1)*3)
        tri = [[n], [n+1, n+(size-1)*3-1]]
        for i in range(len(tmp)):
            tri.append([n+i+2]+tmp[i]+[n+(size-1)*3-2-i])
        tri.append([n+size+i-1 for i in range(size)])
        return tri
def solution(n):
    answer = []
    tmp = triangle(n, 1)
    for t in tmp:
        answer += t
    return answer