def solution(clothes):
    answer = 0
    dic = {}
    for name, where in clothes:
        if dic.get(where):
            dic[where].append(name)
        else:
            dic[where] = [name]
    
    nums = [len(dic[k]) for k in dic]
    answer = 1
    for n in nums:
        answer *= n+1
    answer -= 1
        
    
    return answer