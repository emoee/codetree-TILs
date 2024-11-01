n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
balls = [[0]*n for _ in range(n)]
next_balls = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    balls[r-1][c-1] += 1

def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def find(x, y):
    value = -1
    mx, my = x, y
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if inrange(nx, ny) and board[nx][ny] > value:
            mx, my = nx, ny
            value = board[nx][ny]
    return mx, my

def move(x, y):
    nx, ny = find(x, y)
    next_balls[nx][ny] += 1

for _ in range(t):
    next_balls = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if balls[i][j]:
                move(i, j)

    for i in range(n):
        for j in range(n):
            balls[i][j] = next_balls[i][j]

    for i in range(n):
        for j in range(n):
            if balls[i][j] >= 2:
                balls[i][j] = 0
    
print(sum(row.count(1) for row in balls))