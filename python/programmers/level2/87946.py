answer = 0
N = 0
visit = []


def dfs(k, count, dungeons):
    global answer
    if count > answer:
        answer = count

    for i in range(N):
        if k >= dungeons[i][0] and not visit[i]:
            visit[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons)
            visit[i] = False


def solution(k, dungeons):
    global N, visit
    N = len(dungeons)
    visit = [False] * N
    dfs(k, 0, dungeons)
    return answer
