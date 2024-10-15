n = int(input())

dp = [0] * 46
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = -1
dp[5] = 2
dp[6] = 2
dp[7] = 3

for i in range(8, n+1):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n])