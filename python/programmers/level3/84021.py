import copy
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution(game_board, table):
    answer = 0
    n = len(table)
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 1:
                game_board[i][j] = 0
            else:
                game_board[i][j] = 1

    puzzle = []
    new_table = copy.deepcopy(table)
    for i in range(n):
        for j in range(n):
            if new_table[i][j] == 1:
                new_table[i][j] = 0
                q = deque([[i, j]])
                location = [[i, j]]
                puzzle.append(bfs(new_table, q, location, n))
    new_locations = get_new_locations(puzzle)
    pieces = get_piece_or_space(table, new_locations)

    for _ in range(4):
        # 회전을 위해 4회 반복하고 로직이 끝난 후 남아 있는 pieces를 기반으로 다시 회전해야함
        new_pieces = []
        for piece in pieces:
            new_pieces.append(rotate(piece))
        # 복사본을 통해 상태를 체크하고 최종 값은 원본에 반영해야한다.
        new_game_board = copy.deepcopy(game_board)
        for i in range(n):
            for j in range(n):
                if new_game_board[i][j] == 1:
                    new_game_board[i][j] = 0
                    q = deque([[i, j]])
                    location = [[i, j]]
                    new_locations = get_new_locations([bfs(new_game_board, q, location, n)])
                    space = get_piece_or_space(game_board, new_locations)[0]
                    if space in new_pieces:
                        new_pieces.remove(space)
                        for y_min, x_min, y_max, x_max in new_locations:
                            for y in range(y_min, y_max + 1):
                                for x in range(x_min, x_max + 1):
                                    if game_board[y][x] == 1:
                                        game_board[y][x] = 0
                                        answer += 1
        pieces = new_pieces
    return answer


def bfs(table, q, location, n):
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                if table[ny][nx] == 1:
                    location.append([ny, nx])
                    table[ny][nx] = 0
                    q.append([ny, nx])
    return location


def get_piece_or_space(table, new_locations):
    pieces = []
    for y_min, x_min, y_max, x_max in new_locations:
        piece = []
        for y in range(y_min, y_max + 1):
            row = table[y]
            piece.append(row[x_min: x_max + 1])
        pieces.append(piece)
    return pieces


def get_new_locations(puzzle):
    new_locations = []
    for loc in puzzle:
        y_min = int(1e9)
        x_min = int(1e9)
        y_max = 0
        x_max = 0
        for y, x in loc:
            y_min = min(y_min, y)
            x_min = min(x_min, x)
            y_max = max(y_max, y)
            x_max = max(x_max, x)
        new_locations.append([y_min, x_min, y_max, x_max])
    return new_locations


def rotate(piece):
    row_size = len(piece)
    col_size = len(piece[0])
    rotated_piece = [[0] * row_size for _ in range(col_size)]
    for i in range(row_size):
        for j in range(col_size):
            rotated_piece[j][row_size - i - 1] = piece[i][j]
    return rotated_piece
