def solution(rows, columns, queries):
    answer = []
    count = 0
    maps = initMap(rows, columns)
    while count < len(queries):
        maps = rotate(maps, queries[count], answer)
        count += 1

    return answer


def initMap(rows, columns):
    maps = [[(columns * i) + (j + 1) for j in range(columns)] for i in range(rows)]
    return maps


def rotate(maps, query, answer):
    visit = [[False for j in range(len(maps[0]))] for i in range(len(maps))]
    y1, x1, y2, x2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
    moveY, moveX = y1, x1
    temp = maps[moveY][moveX]
    minNum = 10001
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    d = 0
    while True:
        visit[moveY][moveX] = True
        if (moveY + dy[d] > y2 or moveY + dy[d] < y1) or (moveX + dx[d] > x2 or moveX + dx[d] < x1):
            d = (d + 1) % 4
        moveY += dy[d]
        moveX += dx[d]
        if visit[moveY][moveX]:
            break
        maps[moveY][moveX], temp = temp, maps[moveY][moveX]
        minNum = min(minNum, maps[moveY][moveX])
    answer.append(minNum)
    return maps


if __name__ == "__main__":
    # print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    # print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
    # print(solution(100, 97, [[1,1,100,97]]))

    print(solution(5, 4, [[3, 1, 4, 4]]))
