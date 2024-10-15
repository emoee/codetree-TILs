n = int(input())
MOD = 10007

dp = [0] * max((n+1), 5)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, n+1):
    dp[i] = (dp[i-2] + dp[i-3])%MOD

print(dp[n])