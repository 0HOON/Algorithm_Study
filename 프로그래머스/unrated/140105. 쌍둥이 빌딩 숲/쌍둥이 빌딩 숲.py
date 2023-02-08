# table[a][b] = 2a개 빌딩(n부터 n-a+1)으로 b개 보이게 만드는 경우의 수
# table[a+1][b] = table[a][b] *(2*a) + table[a][b-1]  


def solution(n, count):
    answer = 0
    table = [[0] * (count+1) for _ in range(n+1)]
    table[1][1] = 1
    
    for i in range(2, n+1):
        for j in range(1, min(i+1, count+1)):
            table[i][j] = table[i-1][j] * (2*(i-1)) + table[i-1][j-1]
    return table[n][count] % 1000000007