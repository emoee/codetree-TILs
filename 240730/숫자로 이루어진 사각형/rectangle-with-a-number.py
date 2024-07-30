n = int(input())

board =[[0]*n for _ in range(n)]

number = 0
for i in range(n):
    for j in range(n):
        number += 1
        board[i][j] = number % 10
        if board[i][j] == 0:
            board[i][j] += 1
            number += 1
        

print(board)