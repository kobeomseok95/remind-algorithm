from heapq import heappush, heappop
import sys
read = sys.stdin.readline
INF = int(1e9)
MAX_SIZE = 100_101


def dijkstra(start: int):
    heap = []
    dist[start] = 0
    heappush(heap, (0, start))

    while heap:
        time, point = heappop(heap)
        if point == K:
            break
        if dist[point] < time:
            continue

        for d in range(3):
            if d == 2:
                next_point = point * dx[d]
                next_time = time
            else:
                next_point = point + dx[d]
                next_time = time + 1
            if 0 <= next_point < MAX_SIZE:
                if dist[next_point] > next_time:
                    dist[next_point] = next_time
                    heappush(heap, (next_time, next_point))


N, K = map(int, read().split())
dist = [INF] * MAX_SIZE
dx = [1, -1, 2]

dijkstra(N)
print(dist[K])
