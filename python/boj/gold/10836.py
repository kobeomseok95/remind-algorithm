import sys
read = sys.stdin.readline


M, N = map(int, read().split())
LDU = [(-1, 0), (-1, -1), (-1, 0)]


def solve() -> list:
    bee = [1] * (2 * M - 1)
    for _ in range(N):
        a, b, c = map(int, read().split())
        for idx in range(a, a + b):
            bee[idx] += 1
        for idx in range(a + b, 2 * M - 1):
            bee[idx] += 2

    answer = [[0] * M for _ in range(M)]
    for i, b in enumerate(bee, -M + 1):
        if i >= 0:
            answer[0][i] = b
        else:
            answer[-i][0] = b
    for i in range(1, M):
        for j in range(1, M):
            answer[i][j] = answer[i - 1][j]
    return answer


answer = solve()
for i in range(M):
    for j in range(M):
        print(answer[i][j], end=' ')
    print()