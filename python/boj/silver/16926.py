import sys
read = sys.stdin.readline


def solution(n, m, arr, r):
    for _ in range(r):
        for depth in range(min(n, m) // 2):
            y, x = depth, depth
            tmp = arr[y][x]
            for i in range(depth + 1, n - depth):
                y = i
                prev = arr[y][x]
                arr[y][x] = tmp
                tmp = prev
            for j in range(depth + 1, m - depth):
                x = j
                prev = arr[y][x]
                arr[y][x] = tmp
                tmp = prev
            for i in range(n - depth - 2, depth - 1, -1):
                y = i
                prev = arr[y][x]
                arr[y][x] = tmp
                tmp = prev
            for j in range(m - depth - 2, depth - 1, -1):
                x = j
                prev = arr[y][x]
                arr[y][x] = tmp
                tmp = prev
    return arr


if __name__ == "__main__":
    n, m, r = map(int, read().split())
    arr = [list(map(int, read().split())) for _ in range(n)]
    answer = solution(n, m, arr, r)
    for i in range(n):
        for j in range(m):
            print(answer[i][j], end=' ')
        print()
