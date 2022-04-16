def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        div, mod = divmod(n - 1, 3)
        return solution(div) + '124'[mod]
