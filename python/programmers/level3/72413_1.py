def solution(n, s, a, b, fares):
    graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0
    for y, x, fare in fares:
        graph[y][x] = fare
        graph[x][y] = fare
    for t in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][t] + graph[t][j]:
                    graph[i][j] = graph[i][t] + graph[t][j]
    answer = int(1e9)
    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer
