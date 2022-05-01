import sys
read = sys.stdin.readline


def solution(n, m, arr):
    answer = 0
    for i in range(1, m - 1):
        left, right = max(arr[: i]), max(arr[i + 1:])
        compare = min(left, right)
        if arr[i] < compare:
            answer += compare - arr[i]
    return answer


if __name__ == "__main__":
    n, m = list(map(int, read().split()))
    world = list(map(int, read().split()))
    print(solution(n, m, world))
