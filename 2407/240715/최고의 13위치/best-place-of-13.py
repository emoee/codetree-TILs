n = int(input())

board = [[0]*n for _ in range(n)]
for i in range(n):
    board[i] = (list(map(int, input().split())))

maxValue = 0
for i in range(n):
    for j in range(n-2):
        maxValue = max(maxValue, board[i][j] +  board[i][j+1] +  board[i][j+2])

print(maxValue)