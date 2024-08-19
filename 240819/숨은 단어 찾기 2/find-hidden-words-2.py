n, m = map(int, input().split())

board= [[0]*m for _ in range(n)]

for i in range(n):
    board[i] = list(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

count = 0

dxs, dys = [0, 1, 0, -1, 1, -1, 1, -1], [1, 0, -1, 0, 1, -1, -1, 1]

for x in range(n):
    for y in range(m):
        if in_range(x, y) and board[x][y] == "L":
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and board[nx][ny] == "E":
                    tx, ty = nx + dx, ny + dy
                    if in_range(tx, ty) and board[tx][ty] == "E":
                        count += 1

print(count)