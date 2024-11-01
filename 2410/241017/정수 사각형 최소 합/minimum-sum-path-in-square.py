n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [[0]*n for _ in range(n)]

def init():
    dp[0][n-1] = board[0][n-1]

    for i in range(1, n):
        dp[i][n-1] = board[i][n-1] + dp[i-1][n-1]
        dp[0][(n-1)-i] = board[0][(n-1)-i] + dp[0][n-i]

init()

for i in range(1, n):
    for j in range(1, n):
        dp[i][(n-1)-j] = min(dp[i-1][(n-1)-j] + board[i][(n-1)-j], dp[i][n-j] + board[i][(n-1)-j])

print(dp[n-1][0])