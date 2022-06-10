from collections import deque


def solution(n, computers):
    visit = [False] * n
    answer = 0
    for i in range(n):
        if not visit[i]:
            bfs(computers, visit, n, i)
            answer += 1
    return answer


def bfs(computers, visit, n, point):
    q = deque()
    q.append(point)
    visit[point] = True
    while q:
        cur = q.popleft()
        for i in range(n):
            if cur != i and computers[cur][i] == 1 and not visit[i]:
                q.append(i)
                visit[i] = True
