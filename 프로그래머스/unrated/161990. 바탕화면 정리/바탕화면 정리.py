def solution(wallpaper):
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = -1
    rdy = -1
    for i, row in enumerate(wallpaper):
        for j, r in enumerate(row):
            if r == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i > rdx:
                    rdx = i
                if j > rdy:
                    rdy = j
    
    answer = [lux, luy, rdx+1, rdy+1]
                
    return answer