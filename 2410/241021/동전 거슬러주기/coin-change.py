n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [float('inf')] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for coin in coins:
        if i >= coin:
            if dp[i-coin] == float('inf'):
                continue
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[m] == float('inf'):
    dp[m] = -1

print(dp[m])