import sys
import math
read = sys.stdin.readline
MAX = 1_000_000_000


def init(size: int):
    for i in range(size - 1, 0, -1):
        arr[i] = min(arr[i * 2], arr[i * 2 + 1])


def minimum(start: int, end: int, idx_start: int, idx_end: int, idx_std: int) -> int:
    if start > idx_end or end < idx_start:
        return MAX
    if start <= idx_start and end >= idx_end:
        return arr[idx_std]
    mid = (idx_start + idx_end) // 2
    return min(minimum(start, end, idx_start, mid, idx_std * 2), minimum(start, end, mid + 1, idx_end, idx_std * 2 + 1))


N, M = map(int, read().split())
size = 2 ** math.ceil(math.log(N, 2))
arr = [MAX] * (size * 2)
for i in range(N):
    arr[size + i] = int(read())

init(size)

for _ in range(M):
    s, e = map(int, read().split())
    print(minimum(s-1, e-1, 0, size-1, 1))
