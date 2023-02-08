def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    S_i = None
    for i in range(row_begin-1, row_end):
        if S_i == None:
            S_i = sum(list(map(lambda x: x%(i+1), sorted_data[i])))
        else:
            S_i = S_i ^ sum(list(map(lambda x: x%(i+1), sorted_data[i])))
    
    return S_i