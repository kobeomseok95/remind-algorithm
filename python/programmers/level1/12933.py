def solution(n):
    n = list(str(n))
    n = sorted(n, reverse=True)
    return int("".join(n))
