from collections import deque
import sys
read = sys.stdin.readline
INF = 1e9


def bfs(startY, startX):
    q = deque()
    q.append((startY, startX))
    visit[startY][startX] = 0
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            while True:
                if not (0 <= ny < H and 0 <= nx < W):
                    break
                elif maps[ny][nx] == '*':
                    break
                # 다음 위치가 출발점에서부터 빨리 갈 수 있다면 굳이 갈 이유가 없다.
                elif visit[ny][nx] < visit[y][x] + 1:
                    break
                q.append((ny, nx))
                visit[ny][nx] = visit[y][x] + 1
                ny = ny + dy[d]
                nx = nx + dx[d]


if __name__ == "__main__":
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    W, H = map(int, read().split())
    maps, endpoint = [], []
    for i in range(H):
        maps.append(list(read().strip()))
        for j in range(W):
            if maps[i][j] == 'C':
                endpoint.append((i, j))

    startY, startX, endY, endX = endpoint[0][0], endpoint[0][1], endpoint[1][0], endpoint[1][1]
    visit = [[INF] * W for _ in range(H)]
    bfs(startY, startX)

    print(visit[endY][endX] - 1)
