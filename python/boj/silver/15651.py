import sys
read = sys.stdin.readline


def dfs():
    if len(s) >= M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        s.append(i)
        dfs()
        s.pop()


if __name__ == "__main__":
    N, M = map(int, read().split())
    s = []
    dfs()
