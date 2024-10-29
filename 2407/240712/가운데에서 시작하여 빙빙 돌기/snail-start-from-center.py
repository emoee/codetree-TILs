n = int(input())
board = [[0]* n for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

half = n //2
dirNumber = 0
moveNumber = 1
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0] # 우, 상, 좌, 하

def end():
    return not in_range(x, y)

x, y = half, half
count = 1
while not end():
    for _ in range(moveNumber):
        board[x][y] = count
        x, y = x+dxs[dirNumber], y+dys[dirNumber]
        count += 1
        if end():
            break

    dirNumber = (dirNumber+1) % 4
    if dirNumber == 0 or dirNumber == 2:
        moveNumber += 1

for _ in board:
    print(" ".join(map(str, _)))