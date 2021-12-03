import sys
from collections import deque
read = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(x, count):
    if check[x]:
        if count - dist[x] >= 3:
            return x
        else:
            return -1

    check[x] = 1
    dist[x] = count
    for y in adj[x]:
        node = dfs(y, count + 1)
        if node != -1:
            check[x] = 2
            if x == node:
                return -1
            else:
                return node
    return -1


N = int(read())
adj = [[] * (N + 1) for _ in range(N + 1)]
check = [0] * (N + 1)
dist = [0] * (N + 1)

for _ in range(N):
    u, v = map(int, read().split())
    adj[u].append(v)
    adj[v].append(u)

dfs(1, 0)
q = deque()
for i in range(1, N + 1):
    if check[i] == 2:
        q.append(i)
        dist[i] = 0
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in adj[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(' '.join(map(str, dist[1:])))
