import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
OH_NO = "Oh no"
MIN_COST = 10_000_001


def dfs(x: int, store: list) -> list:
    visit[x] = True
    for n in adj[x]:
        if not visit[n]:
            store.append(n)
            dfs(n, store)
    return store


N, M, K = map(int, read().split())
cost = list(map(int, read().split()))
adj = [[] for _ in range(N)]
for i in range(M):
    v, w = map(int, read().split())
    adj[v - 1].append(w - 1)
    adj[w - 1].append(v - 1)

answer = 0
visit = [False] * N
for i in range(N):
    if not visit[i]:
        min_value = MIN_COST
        store = dfs(i, [i])
        for s in store:
            min_value = min(min_value, cost[s])
        answer += min_value

print(answer if K >= answer else OH_NO)
