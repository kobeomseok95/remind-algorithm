import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline


def dfs(y: int, x: int) -> int:
    if y == M - 1 and x == N - 1:
        return 1
    if visit[y][x] != -1:
        return visit[y][x]
    visit[y][x] = 0
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < M and 0 <= nx < N and maps[y][x] > maps[ny][nx]:
            visit[y][x] += dfs(ny, nx)
    return visit[y][x]


M, N = map(int, read().split())
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
maps = [list(map(int, read().split())) for _ in range(M)]
visit = [[-1] * N for _ in range(M)]
print(dfs(0, 0))
