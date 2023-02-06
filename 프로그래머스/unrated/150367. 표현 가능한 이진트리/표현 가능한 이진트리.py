import math

def check(tree, parent):
    if len(tree) == 1:
        if parent == '1':
            return True 
        else:
            return tree == '0'
    else:
        p = int((len(tree)-1)/2)
        root = tree[p]
        l = tree[:p]
        r = tree[p+1:]
        if parent == '0':
            return root == '0' and check(l, root) and check(r, root)
        else:
            return check(l, root) and check(r, root)
            
        
def solution(numbers):
    answer = []
    numbers_bin = list(map(lambda x: str(bin(x))[2:], numbers))
    for tree in numbers_bin:
        tmp = 1
        while True:
            n = 2**tmp - 1
            if len(tree) > n:
                tmp += 1
                continue
            else:
                tree = '0'*(n-len(tree)) + tree
                break
            
        answer.append(int(check(tree, '1')))
    
    return answer