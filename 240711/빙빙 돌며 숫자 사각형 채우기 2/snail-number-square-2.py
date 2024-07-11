n, m = map(int, input().split())

board = [[0]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 하 우 상 좌
x, y = 0, 0
board[x][y] = 1
dirNumber = 0

for i in range(2, n*m+1):
    nx, ny = x+dxs[dirNumber], y+dys[dirNumber]

    if not in_range(nx, ny) or board[nx][ny] != 0:
        dirNumber = (dirNumber+1) % 4
        
    x, y = x+dxs[dirNumber], y+dys[dirNumber]
    board[x][y] = i

for _ in board:
    print(" ".join(map(str, _)))