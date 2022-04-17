import heapq


def solution(scoville, K):
    if sum(scoville) == 0:
        return -1

    heapq.heapify(scoville)
    count = 0
    while True:
        if len(scoville) >= 1 and scoville[0] >= K:
            return count
        elif len(scoville) == 1:
            return -1

        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        count += 1
        heapq.heappush(scoville, one + (two * 2))
