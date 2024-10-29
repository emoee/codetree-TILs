n = int(input())
board = [[0]*n for _ in range(n)]
numbers = [9, 7, 5, 3, 1]
start = 0

for i in range(n):
    for j in range(n):
        board[i][j] = numbers[start]
        start = (start+1)%5

for b in board:
    print(" ".join(map(str, b)))