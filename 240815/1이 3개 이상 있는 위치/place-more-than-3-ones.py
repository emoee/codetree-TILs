n = int(input())
board = [] * n

for i in range(n):
    board[i] = list(map(int, input().split()))

print(board)