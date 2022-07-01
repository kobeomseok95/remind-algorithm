from collections import defaultdict


def solution(tickets):
    edges = defaultdict(list)
    for start, end in tickets:
        edges[start].append(end)
    for key in edges.keys():
        edges[key].sort()

    return dfs(edges, len(tickets), "ICN", ["ICN"])


def dfs(edges, N, key, routes):
    if len(routes) == N + 1:
        return routes

    for idx, country in enumerate(edges[key]):
        edges[key].pop(idx)
        tmp = routes[:]
        tmp.append(country)
        result = dfs(edges, N, country, tmp)
        edges[key].insert(idx, country)

        if result:
            return result
