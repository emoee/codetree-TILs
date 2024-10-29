n, t = map(int, input().split())
word = list(input())

board = [[0]*n for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

x, y = n//2, n//2
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 상, 우, 하, 좌

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

result = board[x][y]
dirNumber = 0
for i in word:
    nx, ny = x+dxs[dirNumber], y+dys[dirNumber]
    if in_range(nx, ny) and i == "F":
        x, y = nx, ny
        result += board[x][y]
    elif i == "R":
        dirNumber = (dirNumber+1) % 4
    elif i == "L":
        dirNumber = (dirNumber + 3) % 4

print(result)