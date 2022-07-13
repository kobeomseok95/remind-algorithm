from collections import deque


def solution(a, edges):
    answer = 0
    path = find_tree(a, edges)

    for parent, child in path[:-1]:
        child_weight = a[child]
        answer += abs(child_weight)
        a[child] += -child_weight
        a[parent] += child_weight
    if a[0] == 0:
        return answer
    else:
        return -1


def find_tree(a, edges):
    dic = {}
    for v1, v2 in edges:
        if v1 not in dic:
            dic[v1] = []
        if v2 not in dic:
            dic[v2] = []
        dic[v1].append(v2)
        dic[v2].append(v1)

    q = deque([(-1, 0)])
    path = []
    visit = [False] * len(a)
    visit[0] = True
    while q:
        p, c = q.popleft()
        path.append((p, c))
        nxt = dic[c]
        if nxt:
            for n in nxt:
                if not visit[n]:
                    q.append((c, n))
                    visit[n] = True
    return path[::-1]
