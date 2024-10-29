n, t = map(int, input().split())
code = list(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

board = [[0]*n for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y, c = n//2, n//2, 0

result = board[x][y]

for i in code:
    if i == "R":
        c = (c+1) % 4
    elif i == "L":
        c = (c+3) % 4
    else:  
        nx, ny = x + dxs[c], y + dys[c]
        if in_range(nx, ny):
            result += board[nx][ny]
            x, y = nx, ny

print(result)