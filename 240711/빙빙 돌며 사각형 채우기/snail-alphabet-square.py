n, m = map(int, input().split())
board = [[0]*m for _ in range(n)]

dxs, dys = [0, 1, 0, -1],[1, 0, -1 , 0] # 우, 하, 좌, 상
dirNumber = 0
x, y = 0, 0
number = ord('A')
board[x][y] = chr(number)

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n

for i in range(1, n*m):
    nx, ny = x+dxs[dirNumber], y+dys[dirNumber]

    if not in_range(nx, ny) or board[nx][ny] != 0:
        dirNumber = (dirNumber+1) % 4

    x, y = x+dxs[dirNumber], y+dys[dirNumber]
    board[x][y] = chr(number+i)

for _ in board:
    print(" ".join(map(str, _)))