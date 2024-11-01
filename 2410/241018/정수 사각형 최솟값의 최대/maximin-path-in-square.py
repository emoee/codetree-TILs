n = int(input())
board =[list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def init():
    dp[0][0] = board[0][0]
    for i in range(1, n):
        dp[0][i] = min(board[0][i], dp[0][i-1])
        dp[i][0] = min(board[i][0], dp[i-1][0])

init()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], board[i][j]), min(dp[i][j-1], board[i][j]))

print(dp[n-1][n-1])