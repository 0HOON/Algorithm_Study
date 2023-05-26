def solution(msg):
    answer = []
    dic = {chr(c):i+1 for i, c in enumerate(range(ord('A'), ord('Z')+1))}
    i = 0
    while i < len(msg):
        j = i+1
        cc = msg[i]
        while dic.get(cc) != None and j<len(msg):
            cc += msg[j]
            j += 1
        if j < len(msg):
            dic[cc] = len(dic)+1
            answer.append(dic[cc[:-1]])
            i = j-1
        else:
            if dic.get(cc) != None:
                answer.append(dic[cc])
                i = j
            else:
                dic[cc] = len(dic) + 1
                answer.append(dic[cc[:-1]])
                i = j-1
            
    return answer