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


if __name__ == "__main__":
    print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
    print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
    print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
