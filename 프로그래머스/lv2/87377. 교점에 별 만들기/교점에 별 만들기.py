from itertools import combinations

def draw_box(intersection, min_x, min_y, max_x, max_y):
    n_col = max_x - min_x + 1
    n_row = max_y - min_y + 1
    box = [['.']*n_col for _ in range(n_row)]
    star_points = [(y-min_y, x-min_x) for x, y in intersection]
    for i, j in star_points:
        box[i][j] = '*'
    return [''.join(row) for row in box[::-1]]

def solution(line):
    intersection = []
    min_x = float('inf')
    min_y = float('inf')
    max_x = -float('inf')
    max_y = -float('inf')
    for (a, b, e), (c, d, f) in combinations(line, 2):
        if a*d - b*c != 0:
            x = (b*f-e*d)/(a*d-b*c)
            y = (e*c-a*f)/(a*d-b*c)
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                min_x = min(x, min_x)
                min_y = min(y, min_y)
                max_x = max(x, max_x)
                max_y = max(y, max_y)
                intersection.append((x, y))
    answer = draw_box(intersection, min_x, min_y, max_x, max_y)
    return answer