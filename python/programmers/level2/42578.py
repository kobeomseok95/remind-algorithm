from collections import Counter


def solution(clothes):
    count = Counter(category for item, category in clothes)
    answer = 1
    for val in count.values():
        answer *= (val + 1)
    return answer - 1
