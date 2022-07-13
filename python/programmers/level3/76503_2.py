from collections import deque


def solution(a, edges):
    tree = [[] for _ in range(len(a))]
    indegree = [0] * len(a)
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)
        indegree[i] += 1
        indegree[j] += 1

    q = deque()
    for i in range(len(indegree)):
        if indegree[i] == 1:
            q.append(i)
    visit = set()
    answer = 0
    while q:
        cur = q.popleft()
        visit.add(cur)
        for nxt in tree[cur]:
            if nxt not in visit:
                t = a[cur]
                a[cur] -= t
                a[nxt] += t
                answer += abs(t)
                indegree[nxt] -= 1
                if indegree[nxt] == 1:
                    q.append(nxt)

    return answer if sum(a) == 0 else -1
