n, m = map(int, input().split())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

board = [[0]*m for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
c = 0
x, y = 0, 0
board[x][y] = 1
for i in range(2, (n*m+1)):
    nx, ny =  x + dxs[c], y + dys[c]
    
    if not in_range(nx, ny) or board[nx][ny] != 0:
        c = (c+1) % 4
    
    x, y = x + dxs[c], y + dys[c]
    board[x][y] = i
    

for b in board:
    print(" ".join(map(str, b)))