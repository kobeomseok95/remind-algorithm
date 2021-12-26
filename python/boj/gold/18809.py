from collections import deque
from itertools import combinations
from sys import stdin
read = stdin.readline


def bfs(red: list, green: list) -> int:
    red_q, green_q = deque(), deque()
    visit = [[-1] * M for _ in range(N)]
    for r in red:
        visit[r[0]][r[1]] = -2
        red_q.append(r)
    for g in green:
        visit[g[0]][g[1]] = -2
        green_q.append(g)

    flower = 0
    count = 1
    while red_q and green_q:
        for _ in range(len(red_q)):
            y, x = red_q.popleft()
            if visit[y][x] == -100:
                continue
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < M:
                    if visit[ny][nx] == -1 and maps[ny][nx] != 0:
                        visit[ny][nx] = count
                        red_q.append((ny, nx))

        for _ in range(len(green_q)):
            y, x = green_q.popleft()
            if visit[y][x] == -100:
                continue
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < M:
                    if maps[ny][nx] != 0:
                        if visit[ny][nx] == -1:
                            visit[ny][nx] = -2
                            green_q.append((ny, nx))
                        elif visit[ny][nx] == count:
                            visit[ny][nx] = -100
                            flower += 1
        count += 1
    return flower


N, M, G, R = map(int, read().split())
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
maps = []
spreadable = []
for i in range(N):
    inputs = list(map(int, read().split()))
    maps.append(inputs)
    for j in range(M):
        if maps[i][j] == 2:
            spreadable.append((i, j))

answer = 0
for com in combinations(spreadable, G + R):
    for green in combinations(com, G):
        red = [c for c in com if c not in green]
        flower = bfs(red, green)
        answer = max(answer, flower)

print(answer)
