n = int(input())

board = [[0]*n for _ in range(n)]
half = n//2

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

board[half][half] = 1
dirNumber = 0
x, y = half, half
for i in range(2, n*n+1):
    nx, ny = x+dxs[dirNumber], y+dys[dirNumber]

    if not in_range(nx, ny) or board[nx][ny] != 0:
        dirNumber = (dirNumber + 1) % 4
    
    x, y = x+dxs[dirNumber], y+dys[dirNumber]
    board[x][y] = i

for _ in board:
    print(" ".join(map(str, _)))