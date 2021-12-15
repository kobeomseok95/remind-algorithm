import sys
from copy import deepcopy
sys.setrecursionlimit(10**9)
read = sys.stdin.readline


def find_max_value(board: list):
    global ans
    for i in range(N):
        for j in range(N):
            ans = max(ans, board[i][j])


def move_left(board: list):
    for i in range(N):
        p, x = 0, 0
        for j in range(N):
            if board[i][j] == 0:
                continue
            if x == 0:
                x = board[i][j]
            else:
                if x == board[i][j]:
                    board[i][p] = 2 * x
                    x = 0
                    p += 1
                else:
                    board[i][p] = x
                    x = board[i][j]
                    p += 1
            board[i][j] = 0
        if x != 0:
            board[i][p] = x
    return board


def move_right(board: list):
    for i in range(N):
        p, x = N - 1, 0
        for j in range(N - 1, -1, -1):
            if board[i][j] == 0:
                continue
            if x == 0:
                x = board[i][j]
            else:
                if x == board[i][j]:
                    board[i][p] = 2 * x
                    p -= 1
                    x = 0
                else:
                    board[i][p] = x
                    x = board[i][j]
                    p -= 1
            board[i][j] = 0
        if x != 0:
            board[i][p] = x
    return board


def move_up(board: list):
    for i in range(N):
        p, x = 0, 0
        for j in range(N):
            if board[j][i] == 0:
                continue
            if x == 0:
                x = board[j][i]
            else:
                if x == board[j][i]:
                    board[p][i] = 2 * x
                    x = 0
                    p += 1
                else:
                    board[p][i] = x
                    x = board[j][i]
                    p += 1
            board[j][i] = 0
        if x != 0:
            board[p][i] = x
    return board


def move_down(board: list):
    for i in range(N):
        p, x = N - 1, 0
        for j in range(N - 1, -1, -1):
            if board[j][i] == 0:
                continue
            if x == 0:
                x = board[j][i]
            else:
                if x == board[j][i]:
                    board[p][i] = 2 * x
                    p -= 1
                    x = 0
                else:
                    board[p][i] = x
                    x = board[j][i]
                    p -= 1
            board[j][i] = 0
        if x != 0:
            board[p][i] = x
    return board


def dfs(board: list, count: int):
    if count == 5:
        find_max_value(board)
        return
    dfs(move_left(deepcopy(board)), count + 1)
    dfs(move_right(deepcopy(board)), count + 1)
    dfs(move_up(deepcopy(board)), count + 1)
    dfs(move_down(deepcopy(board)), count + 1)


N = int(read())
board = [list(map(int, read().split())) for _ in range(N)]
ans = 0
dfs(board, 0)
print(ans)
