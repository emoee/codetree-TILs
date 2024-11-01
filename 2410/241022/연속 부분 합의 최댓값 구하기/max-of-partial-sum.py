n = int(input())
numbers = list(map(int, input().split()))

dp = [-float('inf')] * (n+1)
dp[0] = 0
dp[1] = numbers[0]

for i in range(2, n+1):
    dp[i] = max(dp[i-1]+numbers[i-1], numbers[i-1])

result = -float('inf')
for i in range(1, n+1):
    result = max(result, dp[i])

print(result)