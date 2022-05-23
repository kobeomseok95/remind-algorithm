from collections import deque


def bfs(start, visit, graph):
    q = deque([start])
    visit[start] = True
    result = 1
    while q:
        point = q.popleft()
        for next_point in graph[point]:
            if not visit[next_point]:
                result += 1
                visit[next_point] = True
                q.append(next_point)
    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for start, visited in wires:
        visit = [False] * (n + 1)
        visit[visited] = True
        result = bfs(start, visit, graph)
        if answer > abs(result - (n - result)):
            answer = abs(result - (n - result))
    return answer
