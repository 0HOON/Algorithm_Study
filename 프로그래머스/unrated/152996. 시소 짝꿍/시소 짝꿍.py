def solution(weights):
    answer = 0
    weight_dict = {}
    
    for w in sorted(weights):
        answer += weight_dict.get(w, 0) + weight_dict.get(w/2, 0) + weight_dict.get(w*2/3, 0) + weight_dict.get(w*3/4, 0)
        weight_dict[w] = weight_dict.get(w, 0) + 1
                
    return answer