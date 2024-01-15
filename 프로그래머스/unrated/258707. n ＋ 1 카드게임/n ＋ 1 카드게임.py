def solution(coin, cards):
    answer = 0
    n = len(cards)
    m = n//3
    memo = [0] * (n//2+1)
    pairs = [0, 0, 0] # coin 0개, coin 1개, coin 2개 이용
    for c in cards[:m]:
        c = min(c, n+1-c)
        memo[c] += 1
        if memo[c] == 2:
            pairs[0] += 1
        
    memo_in = [0] * (n//2 + 1)
    
    for r in range(n//3+1):
        if m + r*2 < len(cards):
            a, b = cards[m+r*2], cards[m+r*2+1]
            a, b = min(a, n+1-a), min(b, n+1-b)
            memo_in[a] += 1
            if memo[a] == 1:
                pairs[1] += 1
            elif memo_in[a] == 2:
                pairs[2] += 1

            memo_in[b] += 1
            if memo[b] == 1:
                pairs[1] += 1
            elif memo_in[b] == 2:
                pairs[2] += 1

        if pairs[0] > 0:
            pairs[0] -= 1
        elif pairs[1] > 0 and coin > 0:
            pairs[1] -= 1
            coin -= 1
        elif pairs[2] > 0 and coin > 1:
            pairs[2] -= 1
            coin -= 2
        else:
            break
        
    return r + 1