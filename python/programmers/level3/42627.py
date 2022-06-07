import heapq
from collections import deque


def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    heap = []
    heapq.heappush(heap, tasks.popleft())
    now, total_response_time = 0, 0
    while heap:
        duration, request_time = heapq.heappop(heap)
        now = max(now + duration, request_time + duration)
        total_response_time += now - request_time
        while len(tasks) > 0 and tasks[0][1] <= now:
            heapq.heappush(heap, tasks.popleft())
        if not heap and tasks:
            heapq.heappush(heap, tasks.popleft())
    return total_response_time // len(jobs)
