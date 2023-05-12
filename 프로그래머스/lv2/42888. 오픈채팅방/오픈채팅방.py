def solution(record):
    answer = []
    memo = {}
    for rec in record:
        tmp = rec.split()
        if len(tmp) > 2:
            op, uid, nickname = tmp
            memo[uid] = nickname
            
    for rec in record:
        tmp = rec.split()
        op, uid = tmp[0], tmp[1]
        if op == 'Enter':
            answer.append(f'{memo[uid]}님이 들어왔습니다.')
        elif op == 'Leave':
            answer.append(f'{memo[uid]}님이 나갔습니다.')
    return answer