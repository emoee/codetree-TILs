n = int(input())
board = [[0] * 10001 for _ in range(101)]

MAXV = 0
MINV = 10001
for i in range(n):
    t = int(input())
    for j in range(t):
        board[i][j] = 1

    MAXV = max(MAXV, t)
    MINV = min(MINV, t)

result = 0
for i in range(MINV, MAXV + 1):
    value = 1
    for j in range(n-1):
        if board[j][i] == 0 and board[j][i] != board[j+1][i]:
            value += 1
            
    result = max(result, value)

print(result)