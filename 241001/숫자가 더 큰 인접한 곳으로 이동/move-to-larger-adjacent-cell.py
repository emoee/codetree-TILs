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
    px, py = 0, 0
    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if inrange(nx, ny) and board[nx][ny] > std:
            std = board[nx][ny]
            px, py = nx, ny
            break

    if px == 0 and py == 0:
        break

    x, y = px, py
    std = board[px][py]
    result.append(std)

print(" ".join(map(str, result)))