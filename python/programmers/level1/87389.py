from math import sqrt


def solution(n):
    for x in range(1, int(sqrt(n)) + 1):
        if n % x == 1:
            return x
    return n - 1
