def solution(m, n, board):
    board = [list(b) for b in board]
    locations = set()
    answer = 0
    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                find_removal_location(i, j, board, locations)
        if not locations:
            break
        answer += len(locations)
        remove(locations, board)
        pull(m, n, board)
        locations = set()
    return answer


def find_removal_location(i, j, board, locations):
    remove_block = board[i][j]
    if remove_block == 'X':
        return
    for y in range(i, i + 2):
        for x in range(j, j + 2):
            if board[y][x] != remove_block:
                return
    locations.add((i, j))
    locations.add((i, j + 1))
    locations.add((i + 1, j))
    locations.add((i + 1, j + 1))


def remove(locations, board):
    for y, x in locations:
        board[y][x] = 'X'


def pull(m, n, board):
    for x in range(n):
        blocks = []
        for y in range(m):
            if board[y][x] != 'X':
                blocks.append(board[y][x])
        for y in range(m - 1, -1, -1):
            board[y][x] = blocks.pop() if blocks else 'X'
