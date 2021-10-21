def solution(rows, columns, queries):
    maps = [[(r * columns) + (c + 1) for c in range(columns)] for r in range(rows)]
    answer = []
    for query in queries:
        query = [q - 1 for q in query]
        tmp = maps[query[0]][query[1]]
        minValue = tmp

        for i in range(query[0] + 1, query[2] + 1):
            maps[i - 1][query[1]] = maps[i][query[1]]
            minValue = min(maps[i][query[1]], minValue)
        for i in range(query[1] + 1, query[3] + 1):
            maps[query[2]][i - 1] = maps[query[2]][i]
            minValue = min(maps[query[2]][i], minValue)
        for i in range(query[2] - 1, query[0] - 1, -1):
            maps[i + 1][query[3]] = maps[i][query[3]]
            minValue = min(maps[i][query[3]], minValue)
        for i in range(query[3] - 1, query[1] - 1, -1):
            maps[query[0]][i + 1] = maps[query[0]][i]
            minValue = min(maps[query[0]][i], minValue)
        maps[query[0]][query[1] + 1] = tmp

        answer.append(minValue)
    return answer


if __name__ == "__main__":
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
    print(solution(3, 4, [[1,2,3,4], [1,1,3,4]]))
    print(solution(100, 97, [[1,1,100,97]]))
