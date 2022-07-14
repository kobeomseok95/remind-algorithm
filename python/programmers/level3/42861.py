from collections import deque


def solution(n, costs):
    costs = sorted(costs, key=lambda x: (x[2]))
    graph = [[] for _ in range(n)]
    answer = 0
    for a, b, c in costs:
        if not connect(a, b, graph):
            answer += c
            graph[a].append(b)
            graph[b].append(a)
    return answer


def connect(a, b, graph):
    visit = [False] * len(graph)
    q = deque()
    q.append(a)
    visit[a] = True
    while q:
        point = q.popleft()
        if point == b:
            return True
        for nxt_point in graph[point]:
            if not visit[nxt_point]:
                q.append(nxt_point)
                visit[nxt_point] = True
    return False
