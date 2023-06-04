def solution(n, words):
    answer = [0, 0]
    memo = {}
    turn = 0
    last = words[0][0]
    for w in words:
        turn += 1
        if memo.get(w) or last[-1]!=w[0]:
            a, b = divmod(turn, n)
            answer = [b, a+1] if b > 0 else [n, a]
            break
        last = w
        memo[w] = True
    return answer