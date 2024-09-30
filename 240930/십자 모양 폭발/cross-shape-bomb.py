n = int(input())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = [[0]*n for _ in range(n)]
r, c = map(int, input().split())

def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(x, y):
    rg = board[x][y]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    board[x][y] = 0

    if rg > 1:
        for i in range(1, rg):
            for dx, dy in zip(dxs, dys):
                nx, ny = (dx*i)+x, (dy*i)+y
                if inrange(nx, ny):
                    board[nx][ny] = 0
        
    return board

def down(result, board):
    for i in range(n):
        endArray = n
        blank = n-1
        for j in range(endArray-1, -1, -1):
            if board[j][i] != 0:
                result[blank][i] = board[j][i]
                blank -= 1
        
    return result
            
board = bomb(r-1, c-1)
result = down(result, board)

for r in result:
    print(" ".join(map(str, r)))