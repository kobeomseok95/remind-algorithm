def solution(n):
    numbers = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in numbers:
            numbers -= set(range(i * 2, n + 1, i))
    return len(numbers)
