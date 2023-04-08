def solution(name, yearning, photo):
    y = {n: ye for n, ye in zip(name, yearning)}
    answer = list(map(lambda p: sum([y.get(n, 0) for n in p]), photo))
    return answer