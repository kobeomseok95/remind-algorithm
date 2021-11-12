import sys
from collections import deque


def bfs(y, x):
    q = deque()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == '*':
            q.append((ny, nx, i))
        if len(q) == 4:
            cross_star[y][x] = 1

    size = 1
    while len(q) == 4:
        answer.append(str(y + 1) + " " + str(x + 1) + " " + str(size))
        for i in range(4):
            point = q.popleft()
            cross_star[point[0]][point[1]] = 1
            ny, nx = point[0] + dy[point[2]], point[1] + dx[point[2]]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == '*':
                q.append((ny, nx, i))
        size += 1


dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, sys.stdin.readline().strip().split())
maps = [list(sys.stdin.readline().strip()) for _ in range(n)]
star = 0
answer = []
cross_star = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == '*':
            star += 1
            bfs(i, j)

star_sum = 0
for i in range(n):
    star_sum += sum(cross_star[i])

if len(answer) == 0 or star != star_sum:
    print(-1)
else:
    print(len(answer))
    for a in answer:
        print(a)
