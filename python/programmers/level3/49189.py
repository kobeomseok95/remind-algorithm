from heapq import heappop, heappush
INF = int(1e9)


def solution(n, edge):
    edges = [[] for _ in range(n + 1)]
    for s, e in edge:
        edges[s].append(e)
        edges[e].append(s)
    dist = dijkstra(1, edges)
    max_dist = max(dist)
    return dist.count(max_dist)


def dijkstra(start, edges):
    dist = [INF] * (len(edges) + 1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cur_dist, point = heappop(heap)
        if dist[point] < cur_dist:
            continue
        for next_point in edges[point]:
            if dist[next_point] > cur_dist + 1:
                dist[next_point] = cur_dist + 1
                heappush(heap, (cur_dist + 1, next_point))
    for i in range(len(dist)):
        if dist[i] >= INF:
            dist[i] = 0
    return dist
