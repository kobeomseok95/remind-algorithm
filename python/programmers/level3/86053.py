import heapq


def solution(operations):
    min_q = []
    max_q = []

    for operation in operations:
        cmd, num = operation.split(" ")
        if cmd == 'I':
            heapq.heappush(min_q, int(num))
            heapq.heappush(max_q, -int(num))
        else:
            if min_q and max_q:
                if int(num) == 1:
                    min_q.remove(-heapq.heappop(max_q))
                    heapq.heapify(min_q)
                else:
                    max_q.remove(-heapq.heappop(min_q))
                    heapq.heapify(max_q)
    return [0, 0] if not min_q else [-heapq.heappop(max_q), heapq.heappop(min_q)]
