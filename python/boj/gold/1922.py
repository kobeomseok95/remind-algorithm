from heapq import heappush, heappop
import sys
read = sys.stdin.readline


def find(x: int) -> int:
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


N = int(read())
M = int(read())
root = [i for i in range(N + 1)]
heap = []
for _ in range(M):
    a, b, c = map(int, read().split())
    heappush(heap, (c, a, b))

answer = 0
while heap:
    c, a, b = heappop(heap)
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        continue
    if root_a > root_b:
        root[root_a] = root_b
    else:
        root[root_b] = root_a
    answer += c

print(answer)
