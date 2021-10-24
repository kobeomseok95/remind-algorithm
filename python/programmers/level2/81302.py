from collections import deque

SIZE = 5
move = ((0, 1), (1, 0), (-1, 0), (0, -1))


def set_up(place):
    arr = []
    seated = []
    for i, string in enumerate(place):
        for j, s in enumerate(string):
            if s == 'P':
                seated.append((i, j))
        arr.append(list(string))
    return arr, seated


def is_in(y, x):
    if -1 < y < SIZE and -1 < x < SIZE:
        return True
    return False


def bfs(arr, sy, sx):
    q = deque()
    q.append((sy, sx))

    table = [[-1 for _ in range(SIZE)] for _ in range(SIZE)]
    table[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + move[i][0]
            nx = x + move[i][1]

            if not is_in(ny, nx):
                continue
            if arr[ny][nx] != 'X' and table[ny][nx] == -1:
                table[ny][nx] = table[y][x] + 1
                q.append((ny, nx))

    return table


def solution(places):
    answer = []
    for place in places:
        arr, seated = set_up(place)
        ok = True

        for sit in seated:
            table = bfs(arr, sit[0], sit[1])
            for other_sit in seated:
                if other_sit != sit:
                    if -1 < table[other_sit[0]][other_sit[1]] <= 2:
                        ok = False
                        break
            if not ok:
                break
        if ok:
            answer.append(1)
        else:
            answer.append(0)

    return answer


if __name__ == "__main__":
    print(solution([
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]))