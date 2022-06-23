import heapq


def solution(n, s, a, b, fares):
    destinations = [[] for _ in range(n + 1)]
    for y, x, fare in fares:
        destinations[y].append((fare, x))
        destinations[x].append((fare, y))
    dp = [[]] + [dijkstra(n, i, destinations) for i in range(1, n + 1)]
    answer = int(1e9)
    for i in range(1, n + 1):
        answer = min(answer, dp[s][i] + dp[i][a] + dp[i][b])
    return answer


def dijkstra(n, s, destinations):
    dist = [int(1e9)] * (n + 1)
    dist[s] = 0
    heap = []
    heapq.heappush(heap, (0, s))
    while heap:
        value, point = heapq.heappop(heap)
        if dist[point] < value:
            continue
        for fare, next_point in destinations[point]:
            next_value = value + fare
            if next_value < dist[next_point]:
                dist[next_point] = next_value
                heapq.heappush(heap, (next_value, next_point))
    return dist
