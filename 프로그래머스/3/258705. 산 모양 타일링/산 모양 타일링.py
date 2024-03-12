# top == 1
#   1. top에 마름모
#       왼쪽 빈칸/왼쪽 마름모 => 왼쪽 빈칸
#   2. top에 세모
#       1) 왼쪽빈칸
#           (1) 세모세모 빈칸 => 왼쪽 빈칸
#           (2) 마름모 빈칸 => 왼쪽 빈칸
#           (3) 세모마름모 => 왼쪽 마름모
#       2) 왼쪽 마름모
#           (1) 세모 빈칸 => 왼쪽 빈칸
#           (2) 마름모 => 왼쪽 빈칸
# top == 0


def solution(n, tops):
    answer = [[0, 0] for _ in range(n+1)] # 왼쪽 빈칸 / 왼쪽 마름모
    answer[0] = [1, 0]
    for i, t in enumerate(tops):
        if t:
            answer[i+1][0] += answer[i][1] + answer[i][0]
            
        answer[i+1][0] += answer[i][0] * 2 + answer[i][1]
        answer[i+1][1] += answer[i][0] + answer[i][1]
        
        answer[i+1][0], answer[i+1][1] = answer[i+1][0]%10007, answer[i+1][1]%10007
        
    return sum(answer[-1])%10007