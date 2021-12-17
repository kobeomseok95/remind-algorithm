import sys
from collections import defaultdict
from heapq import heappush, heappop
INF = int(1e9)
read = sys.stdin.readline


def dijkstra_wolf():
    distance = [[INF] * (N + 1) for _ in range(2)]
    distance[1][1] = 0
    q = []
    heappush(q, (distance[1][1], 1, False))
    while q:
        dist, point, is_fast = heappop(q)
        if is_fast and distance[0][point] < dist:
            continue
        elif not is_fast and distance[1][point] < dist:
            continue
        for nxt_point, nxt_dist in adj[point]:
            if is_fast:
                cost = dist + nxt_dist * 2
                if distance[1][nxt_point] > cost:
                    distance[1][nxt_point] = cost
                    heappush(q, (distance[1][nxt_point], nxt_point, False))
            else:
                cost = dist + nxt_dist // 2
                if distance[0][nxt_point] > cost:
                    distance[0][nxt_point] = cost
                    heappush(q, (distance[0][nxt_point], nxt_point, True))
    return distance


def dijkstra_fox():
    distance = [INF] * (N + 1)
    distance[1] = 0
    q = []
    heappush(q, (distance[1], 1))
    while q:
        dist, point = heappop(q)
        if distance[point] < dist:
            continue
        for nxt_point, nxt_dist in adj[point]:
            cost = dist + nxt_dist
            if distance[nxt_point] > cost:
                distance[nxt_point] = cost
                heappush(q, (distance[nxt_point], nxt_point))
    return distance


N, M = map(int, read().split())
adj = defaultdict(list)
for _ in range(M):
    a, b, d = map(int, read().split())
    adj[a].append((b, d * 2))
    adj[b].append((a, d * 2))

wolf = dijkstra_wolf()
fox = dijkstra_fox()
answer = 0
for i in range(1, N + 1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1
print(answer)
