def get_sequence(k):
    sequence = [k]
    while k > 1:
        if k % 2 == 0:
            k = k/2
        else:
            k = k*3 + 1
            
        sequence.append(k)
    
    return sequence

def get_area(s, e, sequence):
    area = 0
    
    if s >= len(sequence) + e:
        return -1
    
    for i in range(s, len(sequence) + e - 1):
        a = sequence[i]
        b = sequence[i+1]
        area += (a+b)/2
        
    return area

def solution(k, ranges):
    answer = []
    sequence = get_sequence(k)
    for s, e in ranges:
        answer.append(get_area(s, e, sequence))
        
    return answer