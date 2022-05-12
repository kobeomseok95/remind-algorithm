import sys
read = sys.stdin.readline


def dfs(point):
    if len(s) >= M:
        print(' '.join(map(str, s)))
        return
    for i in range(point, N + 1):
        if i not in s:
            s.append(i)
            dfs(i)
            s.pop()


if __name__ == "__main__":
    N, M = map(int, read().split())
    s = []
    dfs(1)
