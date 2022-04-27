import math
from itertools import permutations


def solution(numbers):
    answer = set()
    for case in range(1, len(numbers) + 1):
        for per in set(permutations(numbers, case)):
            number = int(''.join(per))
            if number > 1 and is_prime(number):
                answer.add(number)
    return len(answer)


def is_prime(number):
    for div in range(2, int(math.sqrt(number)) + 1):
        if number % div == 0:
            return False
    return True
