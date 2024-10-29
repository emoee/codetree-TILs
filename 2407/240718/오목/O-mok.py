n = 19
board = [0] * n
for i in range(n):
    board[i] = list(map(int, input().split()))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def who_win(w, b, x, y):
    win = 0
    if b == 5:
        win = 1
    elif w == 5:
        win = 2
    return win, x+1, y+1

def checkX(x, y):
    b, w = 0, 0
    nx = 0
    for i in range(5):
        nx = x+i
        if in_range(nx, y):
            if board[nx][y] == 1:
                b += 1
            elif board[nx][y] == 2:
                w += 1
        else:
            break

    return who_win(w, b, nx-2, y)

def checkY(x, y):
    b, w = 0, 0
    ny = 0
    for i in range(5):
        ny = y+i
        if in_range(x, ny):
            if board[x][ny] == 1:
                b += 1
            elif board[x][ny] == 2:
                w += 1
        else:
            break
    return who_win(w, b, x, ny-2)

def checkL(x, y):
    b, w = 0, 0
    nx, ny = 0, 0
    for i in range(5):
        nx, ny = x-i, y+i
        if in_range(nx, ny):
            if board[nx][ny] == 1:
                b += 1
            elif board[nx][ny] == 2:
                w += 1
        else:
            break
    return who_win(w, b, nx+2, ny-2)

def checkR(x, y):
    b, w = 0, 0
    nx, ny = 0, 0
    for i in range(5):
        nx, ny = x+i, y+i
        if in_range(nx, ny):
            if board[nx][ny] == 1:
                b += 1
            elif board[nx][ny] == 2:
                w += 1
        else:
            break
    return who_win(w, b, nx-2, ny-2)

win, x, y = 0, 0, 0
for i in range(n):
    for j in range(n):
        win, x, y = checkX(i, j)
        if win > 0:
            break
        win, x, y = checkY(i, j)
        if win > 0:
            break
        win, x, y = checkR(i, j)
        if win > 0:
            break
        win, x, y = checkL(i, j)
        if win > 0:
            break
    if win > 0:
        break

print(win)
if win > 0:
    print(x, y)