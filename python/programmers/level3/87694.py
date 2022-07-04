from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    possible_visit = border_points_visit_true(rectangle)
    return bfs(possible_visit, characterY, characterX, itemY, itemX) // 2


def border_points_visit_true(rectangle):
    visit = [[False] * 103 for _ in range(103)]
    for lbx, lby, rtx, rty in rectangle:
        for i in range(lby * 2, rty * 2 + 1):
            for j in range(lbx * 2, rtx * 2 + 1):
                visit[i][j] = True
    for lbx, lby, rtx, rty in rectangle:
        for i in range(lby * 2 + 1, rty * 2):
            for j in range(lbx * 2 + 1, rtx * 2):
                visit[i][j] = False
    return visit


def bfs(possible_visit, characterY, characterX, itemY, itemX):
    q = deque()
    q.append((0, characterY, characterX))
    visits = set()
    visits.add((characterY, characterX))
    while q:
        dist, currentY, currentX = q.popleft()
        if currentY == itemY and currentX == itemX:
            return dist
        for dy, dx in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
            ny, nx = currentY + dy, currentX + dx
            if possible_visit[ny][nx] and (ny, nx) not in visits:
                q.append((dist + 1, ny, nx))
                visits.add((ny, nx))
