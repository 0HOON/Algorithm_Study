from copy import deepcopy as dc

def cal(op, a, b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    
def calculate(nums, ops, priority):
    operators = ['+', '-', '*']
    n = dc(nums)
    o = dc(ops)
    for p in priority:
        op = operators[p]
        tmp_nums = [n[0]]
        tmp_ops = []
        i = 0
        while i < len(o):
            op_ = o[i]
            if op_ == op:
                tmp_nums[-1] = cal(op_, tmp_nums[-1], n[i+1])
            else:
                tmp_ops.append(op_)
                tmp_nums.append(n[i+1])
            i += 1
        n = tmp_nums
        o = tmp_ops
        
    return abs(n[0])

def solution(expression):
    priority = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    nums = []
    ops = []
    n = ''
    for c in expression:
        if c.isdigit():
            n += c
        else:
            if n != '':
                nums.append(int(n))
                n = ''
            ops.append(c)
    nums.append(int(n))
    
    answer = 0
    for p in priority:
        answer = max(answer, calculate(nums, ops, p))

    return answer