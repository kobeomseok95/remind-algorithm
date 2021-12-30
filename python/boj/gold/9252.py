import sys
read = sys.stdin.readline


A = read().strip()
B = read().strip()
a = len(A)
b = len(B)
dp = [[0] * (a + 1) for _ in range(b + 1)]
for i in range(1, b + 1):
    for j in range(1, a + 1):
        if B[i - 1] == A[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[b][a])
answer = []
y = b
x = a
while y > 0 and x > 0:
    if dp[y][x - 1] == dp[y][x]:
        x -= 1
    elif dp[y - 1][x] == dp[y][x]:
        y -= 1
    else:
        answer.append(A[x - 1])
        y -= 1
        x -= 1

for a in answer[::-1]:
    print(a, end='')