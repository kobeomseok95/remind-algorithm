import heapq


def solution(maps):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    visit = set()
    q = [(1, 0, 0)]
    visit.add((0, 0))
    while q:
        block_count, cy, cx = heapq.heappop(q)
        if cy == n - 1 and cx == m - 1:
            return block_count

        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx) not in visit and maps[ny][nx] == 1:
                    visit.add((ny, nx))
                    q.append((block_count + 1, ny, nx))

    return -1
