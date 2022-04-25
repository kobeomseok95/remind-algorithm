import sys
read = sys.stdin.readline


if __name__ == "__main__":
    n = int(read().strip())
    calendar = [0] * 367
    for _ in range(n):
        start, end = map(int, read().split())
        calendar[start] += 1
        calendar[end + 1] -= 1

    width, height, answer = 0, 0, 0
    for day in range(1, 367):
        calendar[day] += calendar[day - 1]
        if calendar[day] == 0:
            answer += width * height
            width, height = 0, 0
        else:
            width += 1
            height = max(height, calendar[day])
    print(answer)
