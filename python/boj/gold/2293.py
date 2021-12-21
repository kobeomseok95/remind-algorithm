import sys
read = sys.stdin.readline


N, K = map(int, read().split())
coins = []
for _ in range(N):
    coins.append(int(read()))
coins.sort()

dp = [0] * (K + 1)
dp[0] = 1
for i in range(N):
    for j in range(coins[i], K + 1):
        dp[j] += dp[j - coins[i]]
print(dp[K])
