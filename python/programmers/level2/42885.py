from collections import deque


def solution(people, limit):
    boat = 0
    people.sort()
    q = deque(people)
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.pop()
                q.popleft()
            else:
                q.pop()
            boat += 1
        else:
            q.pop()
            boat += 1
    return boat
