import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.readline


def dfs(y: int, x: int):
    places[y][x] = 'x'
    if x == C - 1:
        return True

    for dy, dx in move:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and places[ny][nx] != 'x':
            if dfs(ny, nx):
                return True
    return False


R, C = map(int, read().split())
places = [list(map(str, read().strip())) for _ in range(R)]
move = [(-1, 1), (0, 1), (1, 1)]
answer = 0
for i in range(R):
    if dfs(i, 0):
        answer += 1
print(answer)
