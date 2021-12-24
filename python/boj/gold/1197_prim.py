from heapq import heappush, heappop
import sys
read = sys.stdin.readline


def find(x: int) -> int:
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


V, E = map(int, read().split())
edges = []
for _ in range(E):
    a, b, c = map(int, read().split())
    heappush(edges, (c, a, b))

root = [i for i in range(V + 1)]
answer = 0
for _ in range(E):
    c, a, b = heappop(edges)
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        if root_a > root_b:
            root[root_a] = root_b
        else:
            root[root_b] = root_a
        answer += c
print(answer)
