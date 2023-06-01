from collections import deque
def solution(str1, str2):
    answer = 0
    tmp = ''
    set1 = []
    set2 = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            set1.append(str1[i:i+2].lower())    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            set2.append(str2[i:i+2].lower())    
    
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    
    set1 = sorted(set1)
    set2 = sorted(set2)
        
    intersection = 0
    union = 0
    
    set1 = deque(set1)
    set2 = deque(set2)
        
    while len(set1) > 0 or len(set2) > 0:
        if len(set1) == 0:
            union += len(set2)
            break
        elif len(set2) == 0:
            union += len(set1)
            break
            
        if set1[0] == set2[0]:
            intersection += 1
            union += 1
            set1.popleft()
            set2.popleft()
        elif set1[0] > set2[0]:
            union += 1
            set2.popleft()
        elif set1[0] < set2[0]:
            union += 1
            set1.popleft()
    
    answer = int(intersection/union * 65536)
    return answer
