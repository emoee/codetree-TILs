n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1

    board[x][y] = 1
    count = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and board[nx][ny] == 1:
            count += 1
    if count == 3:
        print(1)
    else:
        print(0)