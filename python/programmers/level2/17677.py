def solution(str1, str2):
    MULTIPLE_NUMBER = 65536
    str1_set = create_multiple_set(str1)
    str2_set = create_multiple_set(str2)
    similarity = calculate_jaccard_similarity(str1_set, str2_set)
    return int(similarity * MULTIPLE_NUMBER)


def create_multiple_set(string):
    str_set = []
    for i in range(len(string) - 1):
        sliced = string[i: i+2].lower()
        if sliced.isalpha():
            str_set.append(sliced)
    return str_set


def calculate_jaccard_similarity(str1_set, str2_set):
    intersect = set(str1_set) & set(str2_set)
    union = set(str1_set) | set(str2_set)
    if not intersect and not union:
        return 1
    intersect_sum = sum([min(str1_set.count(i), str2_set.count(i)) for i in intersect])
    union_sum = sum([max(str1_set.count(i), str2_set.count(i)) for i in union])
    return intersect_sum / union_sum
