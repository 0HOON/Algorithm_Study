def LRU(city, n, cache, last_used):
    min_i = 0
    min_l = float('inf')
    for i, l in enumerate(last_used):
        if l < min_l:
            min_l = l
            min_i = i
        if city == cache[i]:
            last_used[i] = n
            return 1
        
    cache[min_i] = city
    last_used[min_i] = n
    return 5


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    cache = ['']*cacheSize
    last_used = [0]*cacheSize    
    answer = 0    
    for i, city in enumerate(cities):
        answer += LRU(city.lower(), i+1, cache, last_used)
    return answer