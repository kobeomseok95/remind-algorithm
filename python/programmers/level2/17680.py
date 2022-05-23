from collections import deque


def solution(cache_size, cities):
    cache = deque(maxlen=cache_size)
    answer = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            cache.append(city)
        else:
            answer += 1
            cache.remove(city)
            cache.append(city)
    return answer
