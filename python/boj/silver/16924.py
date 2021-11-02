import sys


def calc_cross_max_size():
    mini = min(n, m)
    length = mini if mini % 2 != 0 else mini - 1
    return length // 2


def row_check(y, x, size):
    for c in range(x - size, x + size + 1):
        if maps[y][c] != '*':
            return False
    return True


def column_check(y, x, size):
    for r in range(y - size, y + size + 1):
        if maps[r][x] != '*':
            return False
    return True


def check_cross(y, x, size):
    row = row_check(y, x, size)
    column = column_check(y, x, size)
    if row and column:
        position.append((y + 1, x + 1, size))


def confirm_cross_size(size):
    for y in range(size, n - size):
        for x in range(size, m - size):
            check_cross(y, x, size)


def counting():
    cross_max_size = calc_cross_max_size()
    for size in range(1, cross_max_size + 1):
        confirm_cross_size(size)


n, m = map(int, sys.stdin.readline().strip().split(' '))
position = []
maps = []
for _ in range(n):
    maps.append(list(sys.stdin.readline().strip()))

counting()
print(len(position) if len(position) > 0 else -1)
for i in range(len(position)):
    print(' '.join(map(str, position[i])))
