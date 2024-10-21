n, m = map(int, input().split())
numbers = list(map(int, input().split()))

dp = [float('inf')] * (m+1)
dp[0] = 0

for num in numbers:
    for i in range(m, -1, -1):
        if i >= num:
            if dp[i-num] == float('inf'):
                continue
            dp[i] = min(dp[i], dp[i-num]+1)

print(dp[m])