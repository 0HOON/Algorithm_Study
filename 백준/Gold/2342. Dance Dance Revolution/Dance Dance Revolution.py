import sys
from itertools import combinations

sys.setrecursionlimit(1000000)


def move_cost(s, e):
    if s == 0:
        return 2
    diff = abs(s - e)
    if diff == 2:
        return 4
    elif diff == 0:
        return 1
    else:
        return 3


def solve(state, n):
    if n >= len(instructions):
        return 0

    if states[n][mapping[state]] < 4e6:
        return states[n][mapping[state]]

    move_to = instructions[n]

    c1, c2 = 4e6, 4e6

    if state[0] != move_to:
        tmp = tuple(sorted((state[0], move_to)))
        c1 = solve(tmp, n + 1) + move_cost(state[1], move_to)

    if state[1] != move_to:
        tmp = tuple(sorted((state[1], move_to)))
        c2 = solve(tmp, n + 1) + move_cost(state[0], move_to)

    states[n][mapping[state]] = min(c1, c2)
    return states[n][mapping[state]]


instructions = list(map(int, input().split()[:-1]))

mapping = {}
for i, c in enumerate(combinations(range(5), 2)):
    mapping[c] = i
mapping[(0, 0)] = len(mapping)

states = [[4e10] * len(mapping) for _ in range(len(instructions) + 1)]

print(solve((0, 0), 0))
