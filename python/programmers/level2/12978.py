import heapq


def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, (0, 1))
    while heap:
        cost, node = heapq.heappop(heap)
        for next_cost, next_node in adj[node]:
            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                heapq.heappush(heap, (cost + next_cost, next_node))
    return dist


def solution(n, road, k):
    dist = [int(1e9)] * (n + 1)
    dist[1] = 0
    adj = [[] for _ in range(n + 1)]
    for a, b, c in road:
        adj[a].append((c, b))
        adj[b].append((c, a))
    dijkstra(dist, adj)
    return len([d for d in dist if d <= k])
