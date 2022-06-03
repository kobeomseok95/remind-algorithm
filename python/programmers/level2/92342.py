from collections import deque


def solution(n, info):
    answers = bfs(n, info)
    return [-1] if not answers else answers[-1]


def bfs(n, info):
    answers = []
    q = deque([(0, [0] * len(info))])
    max_gap = 0
    while q:
        target_score, arrows = q.popleft()
        if sum(arrows) == n:
            gap = get_score_gap(info, arrows)
            if gap > 0:
                if gap < max_gap:
                    continue
                if gap > max_gap:
                    max_gap = gap
                    answers.clear()
                answers.append(arrows)
        elif sum(arrows) > n:
            continue
        elif target_score == 10:
            arrows_copy = arrows.copy()
            arrows_copy[target_score] = n - sum(arrows)
            q.append((-1, arrows_copy))
        else:
            arrows_copy1 = arrows.copy()
            arrows_copy1[target_score] = 0
            q.append((target_score + 1, arrows_copy1))

            arrows_copy2 = arrows.copy()
            arrows_copy2[target_score] += (info[target_score] + 1)
            q.append((target_score + 1, arrows_copy2))
    return answers


def get_score_gap(apeaches, ryans):
    apeach_score, ryan_score = 0, 0
    for i in range(len(apeaches)):
        if apeaches[i] == 0 and ryans[i] == 0:
            continue
        if apeaches[i] >= ryans[i]:
            apeach_score += (10 - i)
        else:
            ryan_score += (10 - i)
    return ryan_score - apeach_score
