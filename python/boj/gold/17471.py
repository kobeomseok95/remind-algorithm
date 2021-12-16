import collections, sys, itertools
read = sys.stdin.readline


def bfs(cities: list) -> (int, int):
    start = cities[0]
    q = collections.deque([start])
    visit = set([start])
    sums = 0
    while q:
        v = q.popleft()
        sums += population[v]
        for u in adj[v]:
            if u not in visit and u in cities:
                q.append(u)
                visit.add(u)
    return sums, len(visit)


N = int(read())
population = list(map(int, read().split()))
adj = collections.defaultdict(list)
for i in range(N):
    info = list(map(int, read().split()))
    for j in info[1:]:
        adj[i].append(j - 1)

result = int(1e9)
for i in range(1, N // 2 + 1):
    # 왜 절반만 검사하지?
    combis = list(itertools.combinations(range(N), i))
    for combi in combis:
        sum1, v1 = bfs(combi)
        sum2, v2 = bfs([x for x in range(N) if x not in combi])
        if v1 + v2 == N:
            result = min(result, abs(sum1 - sum2))

print(result if result != int(1e9) else -1)
