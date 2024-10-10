n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    dxs, dys = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, 1, 1, -1, -1]
    value = -1
    mx, my = x, y
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if inrange(nx, ny) and board[nx][ny] > value:
            value = board[nx][ny]
            mx, my = nx, ny
    
    return mx, my

for t in range(m):
    c = False
    for x in range(1, (n*n+1)):
        for i in range(n):
            for j in range(n):
                if board[i][j] == x:
                    dx, dy = move(i, j)
                    board[dx][dy], board[i][j] = board[i][j], board[dx][dy]
                    c = True
                    break
            if c:
                break
        c = False
    
for b in board:
    print(" ".join(map(str, b)))