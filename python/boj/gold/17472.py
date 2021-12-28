import pprint
from collections import deque
import sys
read = sys.stdin.readline


def get_lands(i: int, j: int, lands_count: int):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    lands.append((i, j, lands_count))
    land_dict[(i, j)] = lands_count
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M and not visit[ny][nx] and islands[ny][nx] == 1:
                q.append((ny, nx))
                visit[ny][nx] = True
                lands.append((ny, nx, lands_count))
                land_dict[(ny, nx)] = lands_count


def get_edges() -> list:
    edges = []
    for y, x, cur_land in lands:
        for d in range(4):
            dist = 0
            ny, nx = y + dy[d], x + dx[d]
            while True:
                if 0 <= ny < N and 0 <= nx < M:
                    to_land = land_dict.get((ny, nx))
                    if to_land == cur_land:
                        break
                    elif to_land is None:
                        ny += dy[d]
                        nx += dx[d]
                        dist += 1
                        continue
                    else:
                        if dist < 2:
                            break
                        edges.append((dist, cur_land, to_land))
                        break
                else:
                    break
    return edges


def find(x: int) -> int:
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(a: int, b: int):
    a = find(a)
    b = find(b)
    parents[a] = b


N, M = map(int, read().split())
islands = [list(map(int, read().split())) for _ in range(N)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
land_dict = dict()
lands = []
lands_count = 1
visit = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if islands[i][j] == 1 and not visit[i][j]:
            get_lands(i, j, lands_count)
            lands_count += 1

edges = sorted(get_edges(), reverse=True)

ans = 0
cnt = lands_count - 2
parents = [i for i in range(lands_count)]
while cnt:
    try:
        w, a, b = edges.pop()
    except:
        print(-1)
        sys.exit()
    if find(a) != find(b):
        union(a, b)
        ans += w
        cnt -= 1
print(ans)
