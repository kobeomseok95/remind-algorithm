def solution(rows, columns, queries):
    matrix = init_matrix(rows, columns)
    return [rotate(matrix, query) for query in queries]


def init_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(1, columns + 1):
            row.append(i * columns + j)
        matrix.append(row)
    return matrix


def rotate(matrix, query):
    changed_elements = set()
    y1, x1, y2, x2 = query
    y1 -= 1
    x1 -= 1
    y2 -= 1
    x2 -= 1
    tmp = matrix[y1][x1]
    changed_elements.add(tmp)
    for j in range(x1 + 1, x2 + 1):
        matrix[y1][j], tmp = tmp, matrix[y1][j]
        changed_elements.add(tmp)
    for i in range(y1 + 1, y2 + 1):
        matrix[i][x2], tmp = tmp, matrix[i][x2]
        changed_elements.add(tmp)
    for j in range(x2 - 1, x1 - 1, -1):
        matrix[y2][j], tmp = tmp, matrix[y2][j]
        changed_elements.add(tmp)
    for i in range(y2 - 1, y1 - 1, -1):
        matrix[i][x1], tmp = tmp, matrix[i][x1]
        changed_elements.add(tmp)
    return min(changed_elements)
