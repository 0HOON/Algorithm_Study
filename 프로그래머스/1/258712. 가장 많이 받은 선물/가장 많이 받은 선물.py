def solution(friends, gifts):
    answer = 0
    
    gift_history = {f: {ff: 0 for ff in friends if ff != f} for f in friends}
    
    for a_b in gifts:
        a, b = a_b.split()
        
        gift_history[a][b] += 1
        gift_history[b][a] -= 1
    
    for f in gift_history:
        gift_score = 0
        total_gift = 0
        for ff in gift_history[f]:
            gift_score += gift_history[f][ff]
            if gift_history[f][ff] > 0:
                total_gift += 1
                
        gift_history[f]['gift_score'] = gift_score
        gift_history[f]['total_gift'] = total_gift
    
    answer = 0
    
    for f in gift_history:
        total = 0
        for ff in gift_history[f]:
            if ff == 'gift_score' or ff == 'total_gift':
                continue
                
            if gift_history[f][ff] == 0 and gift_history[f]['gift_score'] > gift_history[ff]['gift_score']:
                gift_history[f]['total_gift'] += 1
                
        if gift_history[f]['total_gift'] > answer:
            answer = gift_history[f]['total_gift']
    
    return answer