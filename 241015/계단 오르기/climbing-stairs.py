n = int(input())
MOD = 10007

dp = [0] * max((n+1), 5)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i] = (dp[i-2] + dp[i-3])%MOD

print(dp[n])