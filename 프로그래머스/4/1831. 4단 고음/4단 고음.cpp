// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
#include<cmath>
#include<iostream>
int count(int n, int m, int p, int m_max, int p_max){
    if (2*m > p){
        //std::cout << 1 << std::endl;
        return 0;
    }
    if ((n == 1) & (m == m_max) & (p == p_max)){
        //std::cout << 2 << std::endl;
        return 1;
    }
    int res = 0;
    if ((m < m_max) & (n%3 == 0)){
        res += count(n/3, m+1, p, m_max, p_max);
    }
    if ((p < p_max) & (n > 0)){
        res += count(n-1, m, p+1, m_max, p_max);
    }
    return res;
}

int solution(int n) {
    float tmp = log((n+1.)/2)/log(3);
    int k;
    if (float(int(tmp)) == tmp){
        k = int(tmp);
    } else {k = int(tmp)+1;}
    //std::cout << k << std::endl;
    int answer = count(n-2, 0, 2, k, 2*k);
    return answer;
}

