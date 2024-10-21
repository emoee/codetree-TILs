n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [float('inf')] * (m+1)
dp[0] = 0

for coin in coins:
    dp[coin] = 1

for i in range(1, m+1):
    for coin in coins:
        if i >= coin:
            if dp[i-coin] == float('inf'):
                continue
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[m])