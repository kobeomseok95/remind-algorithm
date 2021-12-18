import sys
sys.setrecursionlimit(10**6)


def compression(y, x, length, arr, answer):
    start = arr[y][x]
    for i in range(y, y + length):
        for j in range(x, x + length):
            if arr[i][j] != start:
                length //= 2
                compression(y, x, length, arr, answer)
                compression(y, x + length, length, arr, answer)
                compression(y + length, x, length, arr, answer)
                compression(y + length, x + length, length, arr, answer)
                return
    answer[start] += 1


def solution(arr):
    answer = [0, 0]
    length = len(arr)
    compression(0, 0, length, arr ,answer)
    return answer


if __name__ == "__main__":
    print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
    print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
