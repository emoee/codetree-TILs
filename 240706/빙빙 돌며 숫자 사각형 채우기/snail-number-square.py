n, m = map(int, input().split())

board = [[0]*n for _ in range(m)]
# n = 행, m = 열
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# x = 행, y = 열 
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
move = 0
board[0][0] = 1
for i in range(2, n*m+1):
    nx, ny = x+dxs[move], y+dys[move]
    if not in_range(nx, ny) or board[nx][ny] != 0:
        move = (move + 1) % 4

    x, y = x+dxs[move], y+dys[move]
    board[x][y] = i

for i in board:
    print(" ".join(map(str, i)))