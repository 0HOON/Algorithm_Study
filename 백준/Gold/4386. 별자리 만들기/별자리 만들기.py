from itertools import combinations
from copy import deepcopy

def add_star(dist_list):
    # dist_list
    #   -1: added
    #   10e6: not added yet
    #   else: distance
    min_dist = 1e6
    for i, d in enumerate(dist_list):
        if d > 0 and d < min_dist:
            min_dist = d
            next_star = i

    dist_list[next_star] = -1
    for i, d in enumerate(dist_list):
        if d > 0 and mat[next_star][i] < d:
            dist_list[i] = mat[next_star][i]

    return min_dist
            

def dist(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

n = int(input())
mat = [[-1]*n for _ in range(n)]
coordinates = []

for i in range(n):
    x, y = list(map(float, input().split()))
    coordinates.append((x, y))
    mat[i][i] = 0

for i1, i2 in combinations(range(n), 2):
    d = dist(coordinates[i1], coordinates[i2])
    mat[i1][i2] = d
    mat[i2][i1] = d

dist_list = deepcopy(mat[0])
dist_list[0] = -1

res = 0
for _ in range(n-1):
    res += add_star(dist_list)

print(res)