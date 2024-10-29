n, t = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(2)
]

for time in range(t):
    first = board[0][n-1]
    second = board[1][n-1]

    for i in range(n-1, 0, -1):
        board[0][i] = board[0][i-1]

    for i in range(n-1, 0, -1):
        board[1][i] = board[1][i-1]

    board[0][0] = second
    board[1][0] = first

for row in board:
    print(" ".join(map(str, row)))