def solution(triangle):
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(dp)):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][0]
            elif j == i:
                dp[i][j] = dp[i - 1][-1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])
            dp[i][j] += triangle[i][j]
    return max(dp[-1])
