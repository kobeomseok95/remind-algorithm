import math
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline


def odd_count(n):
    count = 0
    for i in n:
        if int(i) % 2 != 0:
            count += 1
    return count


def solution(n, count):
    global min_val, max_val

    if len(n) == 1:
        min_val = min(min_val, count)
        max_val = max(max_val, count)
    elif len(n) == 2:
        string = str(int(n[0]) + int(n[1]))
        solution(string, count + odd_count(string))
    else:
        for i in range(len(n) - 2):
            for j in range(i + 1, len(n) - 1):
                a = n[:i + 1]
                b = n[i + 1: j + 1]
                c = n[j + 1:]
                string = str(int(a) + int(b) + int(c))
                solution(string, count + odd_count(string))
    return min_val, max_val


if __name__ == "__main__":
    n = read().strip()
    min_val, max_val = math.inf, 0
    print(solution(n, odd_count(n)))
