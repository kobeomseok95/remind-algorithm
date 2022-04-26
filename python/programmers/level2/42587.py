from collections import deque


def solution(priorities, location):
    q = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    count = 1
    while q:
        doc = q.popleft()
        if any(doc[0] < docs[0] for docs in q):
            q.append(doc)
        else:
            if doc[1] == location:
                return count
            count += 1
    return count
