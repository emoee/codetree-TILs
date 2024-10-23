n = int(input())
numbers = list(map(int, input().split()))

dp = [[0]*(4) for _ in range(max(n+1, 3))]

dp[1][1] = numbers[0]
dp[2][0] = numbers[1] # 2계단 올라가기
dp[2][2] = numbers[0] + numbers[1] # 1계단 + 1계단 올라가기

for i in range(3, n+1):
    for j in range(4):
        if dp[i-2][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i-2][j]+numbers[i-1])
        if j and dp[i-1][j-1] != 0 :
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + numbers[i-1])

print(max(dp[n]))