def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def get_gcd(array):
    ans = array[0]
    for n in array:
        if ans > n:
            ans = gcd(ans, n)
        else:
            ans = gcd(n, ans)
    return ans

def check_array(gcd, array):
    if gcd == 1:
        return 0
    
    for a in range(gcd, 0, -1):
        if gcd % a == 0:
            c = True
            for b in array:
                if b % gcd == 0:
                    c = False
                    break
            if c:
                return a
    
    return 0

def solution(arrayA, arrayB):
    answer = 0
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    answer = max(check_array(gcdA, arrayB), check_array(gcdB, arrayA))
    return answer