def solution(lottos, win_nums):
    answer = []
    correct = 0
    n_0 = 0
    for n in lottos:
        if n == 0:
            n_0 += 1
        elif n in win_nums:
            correct += 1
    answer = [min(6, 7-correct-n_0), min(6, 7-correct)]
    return answer