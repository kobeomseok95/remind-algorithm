from collections import Counter
from functools import reduce


def solution(clothes):
    count_by_categories = Counter([category for clothes, category in clothes])
    return reduce(lambda x, y: x * (y + 1), count_by_categories.values(), 1) - 1
