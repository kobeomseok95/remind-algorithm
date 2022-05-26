def solution(dirs):
    move = {
        "U": (1, 0),
        "D": (-1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }
    point = [0, 0]
    visit = set()
    for dir in dirs:
        next_y = move[dir][0]
        next_x = move[dir][1]
        start = tuple(point)
        if enable_move(point, next_y, next_x):
            point[0] += move[dir][0]
            point[1] += move[dir][1]
            end = tuple(point)
            visit.add(start + end)
            visit.add(end + start)
    return len(visit) // 2


def enable_move(point, next_y, next_x):
    return -5 <= point[0] + next_y <= 5 and -5 <= point[1] + next_x <= 5
