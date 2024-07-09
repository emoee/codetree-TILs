n = int(input())
board = [input() for _ in range(n)]
start = int(input())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x, y, n):
    dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1] # 하, 좌, 상, 우
    nx, ny = x+dxs[n], y+dys[n]
    return nx, ny, n

def init(start): # return x, y, dir
    if start <= n:
        return 0, start-1, 0
    elif start <= 2 * n:
        return start - n - 1 , n-1, 1
    elif start < 3 * n:
        return n - 1, n - (start - 2 * n), 2
    else:
        return n - (start - 3 * n), 0 , 3

count = 0
x, y, move_dir = init(start)
while in_range(x, y):
    count += 1
    if board[x][y] == "/":
        x, y, move_dir = move(x, y, move_dir ^ 1)
    else: 
        x, y, move_dir = move(x, y, 3 - move_dir)

print(count)