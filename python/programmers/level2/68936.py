def solution(arr):
    answer = [0, 0]
    N = len(arr)
    compress(arr, answer, 0, 0, N)
    return answer


def compress(arr, answer, y, x, N):
    element = arr[y][x]
    for i in range(y, y + N):
        for j in range(x, x + N):
            if arr[i][j] != element:
                NN = N // 2
                compress(arr, answer, y, x, NN)
                compress(arr, answer, y, x + NN, NN)
                compress(arr, answer, y + NN, x, NN)
                compress(arr, answer, y + NN, x + NN, NN)
                return
    if element == 0:
        answer[0] += 1
    else:
        answer[1] += 1
