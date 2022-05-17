def calculate_end_number(n):
    number = 0
    for i in range(n, 0, -1):
        number += i
    return number


def change_dir(y, x, move_y, move_x, arr):
    if y + move_y >= len(arr):
        return True
    if x + move_x >= len(arr[y]):
        return True
    next_y = y + move_y
    next_x = x + move_x
    if arr[next_y][next_x] != 0:
        return True
    return False


def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    y, x = 0, 0
    dirs = [(1, 0), (0, 1), (-1, -1)]
    dir = 0
    end_number = calculate_end_number(n)
    number = 1
    while number <= end_number:
        arr[y][x] = number
        if change_dir(y, x, dirs[dir][0], dirs[dir][1], arr):
            dir = (dir + 1) % 3
        y += dirs[dir][0]
        x += dirs[dir][1]
        number += 1
    answer = []
    for a in arr:
        answer.extend(a)
    return answer
