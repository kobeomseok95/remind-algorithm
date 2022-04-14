import math


# def solution(n):
#     sqrt = math.sqrt(n)
#     return int(sqrt + 1) ** 2 if sqrt == math.sqrt(n) else -1

def solution(n):
    return (n ** 0.5 + 1) ** 2 if (n ** 0.5) % 1 == 0 else -1
