def HNT(f):
    part = 0
    res = []
    for i, c in enumerate(f):
        if part == 0 and c.isdigit():
            res.append(f[:i])
            part = 1
            ii = i
        if part == 1:
            if i == len(f)-1:
                res.append(f[ii:])
            elif not c.isdigit():
                res.append(f[ii:i])
                res.append(f[i:])
                break
    return res
            
def solution(files):
    answer = []
    files = [HNT(f) for f in files]
    answer = sorted(files, key=lambda x: (x[0].lower(), int(x[1])))
    answer = [''.join(f) for f in answer]
    return answer