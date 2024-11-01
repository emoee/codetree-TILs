n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
order = 1

def inrange(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(x, y):
    global order

    dxs, dys = [1, 0], [0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 0:
            visited[nx][ny] = True
            board[nx][ny] = order
            order += 1
            dfs(nx, ny)

visited[0][0] = True
dfs(0, 0)

if board[n-1][m-1] > 1:
    print(1)
else:
    print(0)