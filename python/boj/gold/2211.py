from heapq import heappush, heappop
import sys
read = sys.stdin.readline
INF = int(1e9)


def dijkstra(x: int) -> list:
    dp = [INF] * (N + 1)
    dp[x] = 0
    distance = [0] * (N + 1)
    heap = []
    heappush(heap, (0, x))
    while heap:
        dist, point = heappop(heap)
        for next_point, next_dist in adj[point]:
            cost = dist + next_dist
            if dp[next_point] > cost:
                dp[next_point] = cost
                distance[next_point] = point
                heappush(heap, (cost, next_point))
    return distance


N, M = map(int, read().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, read().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

distance = dijkstra(1)
print(N - 1)
for i in range(2, N + 1):
    print(i, distance[i])
