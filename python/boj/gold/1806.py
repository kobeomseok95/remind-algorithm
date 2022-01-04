import sys
read = sys.stdin.readline


N, S = map(int, read().split())
arr = list(map(int, read().split()))
sum_arr = [0] * (N + 1)
for i in range(1, N + 1):
    sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

answer = N + 1
start, end = 0, 1
while start != N:
    if sum_arr[end] - sum_arr[start] >= S:
        if end - start < answer:
            answer = end - start
        start += 1
    else:
        if end >= N:
            start += 1
        else:
            end += 1

print(answer if answer != N + 1 else 0)
