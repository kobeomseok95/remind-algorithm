import sys
read = sys.stdin.readline


def find(v: int):
    if v_root[v] != v:
        v_root[v] = find(v_root[v])
    return v_root[v]


V, E = map(int, read().split())
edges = [tuple(map(int, read().split())) for _ in range(E)]

v_root = [i for i in range(V + 1)]
edges.sort(key=lambda x: x[2])

answer = 0
for s, e, w in edges:
    s_root = find(s)
    e_root = find(e)
    if s_root != e_root:
        if s_root > e_root:
            v_root[s_root] = e_root
        else:
            v_root[e_root] = s_root
        answer += w
print(answer)
