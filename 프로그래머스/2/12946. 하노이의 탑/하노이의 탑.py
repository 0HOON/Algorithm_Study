from collections import deque
from copy import deepcopy

def move(memo, a, b, n):
    if memo.get((a, b, n)) is not None:
        return memo[(a, b, n)]
    if n == 1:
        return [[a, b]]
    c = 6 - a - b
    return move(memo, a, c, n-1) + [[a, b]] + move(memo, c, b, n-1) 

def solution(n):
    memo = {}
    return move(memo, 1, 3, n)