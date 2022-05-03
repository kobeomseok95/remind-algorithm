from itertools import combinations


def solution(relation):
    row_length = len(relation)
    column_length = len(relation[0])

    candidates = []
    for i in range(1, column_length + 1):
        candidates.extend(combinations(range(column_length), i))

    unique = []
    for candidate in candidates:
        tmp = [tuple([item[key] for key in candidate]) for item in relation]
        if len(set(tmp)) == row_length:
            put = True

            for x in unique:
                if set(x).issubset(set(candidate)):
                    put = False
                    break

            if put:
                unique.append(candidate)

    return len(unique)
