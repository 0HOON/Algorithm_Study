from itertools import accumulate
from collections import deque

def max_sum(seq):
    cumsum = [0] + list(accumulate(seq))
    local_max = -float('inf')
    local_min = float('inf')
    for s in cumsum:
        if s > local_max:
            local_max = s
        if s < local_min:
            local_min = s
    
    return local_max - local_min
    
                

def solution(sequence):
    seq1 = [s if i%2==0 else -s for i, s in enumerate(sequence)]
    #seq2 = [s if i%2==1 else -s for i, s in enumerate(sequence)]
    
    #return max(max_sum(seq1), max_sum(seq2))
    return max_sum(seq1)