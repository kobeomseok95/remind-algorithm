def solution(stones, k):
    start, end = 1, 200_000_001
    answer = end
    while start <= end:
        mid = (start + end) // 2
        if cross_friends(stones, k, mid):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer


def cross_friends(stones, k, mid):
    count = 0
    for stone in stones:
        if stone - mid < 0:
            count += 1
            if count >= k:
                return False
        else:
            count = 0
    return True
