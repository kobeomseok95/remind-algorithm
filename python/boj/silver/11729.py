import sys


def hanoi(num, start, end):
    if num == 1:
        return f'{start} {end}\n'
    if (num, start, end) in cache:
        return cache[(num, start, end)]

    p = 6 - start - end
    cur = [
        hanoi(num - 1, start, p),
        f'{start} {end}\n',
        hanoi(num - 1, p, end)
    ]
    cache[(num, start, end)] = ''.join(cur)
    return cache[(num, start, end)]


cache = {}
n = int(sys.stdin.readline().strip())
print(2 ** n - 1)
print(hanoi(n, 1, 3))
