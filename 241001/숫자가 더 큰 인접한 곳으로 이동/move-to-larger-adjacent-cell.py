n, r, c = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
def inrange(x, y):
    return 0 <= x < n and 0 <= y < n
    
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
std = board[r-1][c-1]
x, y = r-1, c-1

result = [std]
while True:
    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if inrange(nx, ny) and board[nx][ny] > std:
            x, y = nx, ny
            break

    if board[x][y] == std:
        break

    std = board[x][y]
    result.append(std)

print(" ".join(map(str, result)))