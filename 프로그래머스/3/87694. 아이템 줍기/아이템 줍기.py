from itertools import combinations

def get_cross_point(l1, l2):
    (x11, y11), (x12, y12) = l1
    (x21, y21), (x22, y22) = l2
    if (x11 == x12 and x21 == x22) or (y11 == y12 and y21 == y22):  # 평행하면 X
        return None
    
    if x11 != x12: # l1 is horizontal
        if (y21 < y11 and y22 > y11) and (x11 < x21 and x12 > x21):
            return (x21, y11)
    else:           # l1 is vertical
        if (y11 < y21 and y12 > y21) and (x21 < x11 and x22 > x11):
            return (x11, y21)
    
    return None

def comp(a, b, direction):
    if direction == 0:  #right
        if a[0] == b[0] and a[1] < b[1]:
            return 0
        elif a[0] == b[0] and a[1] > b[1]:
            return 1
    elif direction == 2:    #left
        if a[0] == b[0] and a[1] < b[1]:
            return 1
        elif a[0] == b[0] and a[1] > b[1]:
            return 0
    elif direction == 3:    #up
        if a[1] == b[1] and a[0] < b[0]:
            return 1
        elif a[1] == b[1] and a[0] > b[0]:
            return 0
    elif direction == 1:    #down
        if a[1] == b[1] and a[0] < b[0]:
            return 0
        elif a[1] == b[1] and a[0] > b[0]:
            return 1
    
    return -1
        
def find_next_point(point, direction, points):
    x, y = point
    candidate = [[], []]
    
    for p in points:
        tmp = comp(point, p, direction)
        if tmp == 0: # 왼쪽
            candidate[0].append(p)
        elif tmp == 1: # 오른쪽
            candidate[1].append(p)
    
    if len(candidate[0]) > 0:
        next_point = sorted(candidate[0], key=lambda p: abs(x-p[0]) + abs(y-p[1]))[0]
        next_dir = (direction - 1) % 4
    else:
        next_point = sorted(candidate[1], key=lambda p: abs(x-p[0]) + abs(y-p[1]))[0]
        next_dir = (direction + 1) % 4
        
    return next_point, next_dir

def is_between(p1, p2, p):
    if p1[1] == p2[1]:
        return ((p1[0] - p[0]) * (p2[0] - p[0]) <= 0) and p1[1] == p[1]
    else:
        return ((p1[1] - p[1]) * (p2[1] - p[1]) <= 0) and p1[0] == p[0]
    
def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def solve(points, ch, item):
    start_point = max(points, key=lambda x: (x[1], x[0])) #가장 오른쪽 위의 점에서 시작
    # 보고 있는 방향 0, 1, 2, 3 = right, down, left, up
    point, direction = start_point, 0
    
    outer_points = []
    total_dist = 0
    d = 0
    
    found_ch = False
    found_item = False
    
    #dd = ["right", "down", "left", "up"]
    while True:
        #print(point, dd[direction], total_dist, d, found_ch, found_item)
        outer_points.append(point)
        next_point, next_direction = find_next_point(point, direction, points)
        total_dist += dist(point, next_point)
        
        if is_between(point, next_point, ch) and is_between(point, next_point, item):
            d += dist(ch, item)
            found_item = True
            found_ch = True
        elif not found_ch and is_between(point, next_point, ch):
            if not found_item:
                d += dist(ch, next_point)
            else:
                d += dist(ch, point)
            found_ch = True
        elif not found_item and is_between(point, next_point, item):
            if not found_ch:
                d += dist(item, next_point)
            else:
                d += dist(item, point)
            found_item = True
        
        elif found_ch != found_item:
            d += dist(point, next_point)
        
        point = next_point
        direction = next_direction
        
        if point == start_point:
            break
    
    return min(d, total_dist - d)

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    points = []
    for lx, ly, rx, ry in rectangle:
        points.append((lx, ly))
        points.append((lx, ry))
        points.append((rx, ry))
        points.append((rx, ly))
    
    for a, b in combinations(rectangle, 2):
        line_list_1 = []
        line_list_2 = []
        line_list_1.append(((a[0], a[1]), (a[0], a[3])))
        line_list_1.append(((a[0], a[3]), (a[2], a[3])))
        line_list_1.append(((a[2], a[1]), (a[2], a[3])))
        line_list_1.append(((a[0], a[1]), (a[2], a[1])))
        line_list_2.append(((b[0], b[1]), (b[0], b[3])))
        line_list_2.append(((b[0], b[3]), (b[2], b[3])))
        line_list_2.append(((b[2], b[1]), (b[2], b[3])))
        line_list_2.append(((b[0], b[1]), (b[2], b[1])))
        for l1 in line_list_1:
            for l2 in line_list_2:
                point = get_cross_point(l1, l2)
                if point is not None:
                    points.append(point)
    
    ch = (characterX, characterY)
    item = (itemX, itemY)
    
    answer = solve(points, ch, item)
        
        
    return answer