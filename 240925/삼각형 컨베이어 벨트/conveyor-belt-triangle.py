n, time = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(3)
]

for _ in range(time):
    first = board[0][n-1]
    second = board[1][n-1]
    third = board[2][n-1]

    for f in range(n-1, 0, -1):
        board[0][f] = board[0][f-1]

    for s in range(n-1, 0, -1):
        board[1][s] = board[1][s-1]

    for t in range(n-1, 0, -1):
        board[2][t] = board[2][t-1]

    board[0][0] = third
    board[1][0] = first 
    board[2][0] = second

for row in board:
    print(" ".join(map(str, row)))