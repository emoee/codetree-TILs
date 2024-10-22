n = int(input())
numbers = [1, 2, 5]

dp = [0] * max(4, n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    for num in numbers:
        if i >= num:
            dp[i] = (dp[i]+dp[i-num])%10007

print(dp[n])