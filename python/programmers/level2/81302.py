from collections import deque


def solution(places):
    answer = []
    for place in places:
        maps = [list(p) for p in place]
        answer.append(is_follow_distance_rules(maps))
    return answer


def is_follow_distance_rules(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'P':
                if not bfs(maps, i, j):
                    return 0
    return 1


def bfs(maps, i, j):
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((0, i, j))
    visit = set()
    visit.add((i, j))
    while q:
        manhattan_distance, y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < 5 and 0 <= nx < 5 and (ny, nx) not in visit and manhattan_distance < 2:
                if maps[ny][nx] == 'O':
                    q.append((manhattan_distance + 1, ny, nx))
                elif maps[ny][nx] == 'P':
                    return False
    return True
