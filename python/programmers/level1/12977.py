from itertools import combinations
from math import sqrt


def solution(nums):
    return sum(1 if is_prime(sum(com)) else 0 for com in combinations(nums, 3))


def is_prime(result):
    a = int(sqrt(result))
    for i in range(2, a + 1):
        if result % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(solution([1, 2, 7, 6, 4]))
