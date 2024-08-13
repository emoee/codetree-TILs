MAX_R = 2000
board = [[0]* (MAX_R+1) for _ in range(MAX_R+1)]

for i in range(1, 3):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000
    for j in range(x1, x2):
        for k in range(y1, y2):
            board[j][k] = i


x, y, mx, my = MAX_R, MAX_R, 0, 0
rect = False

for i in range(MAX_R+1):
    for j in range(MAX_R+1):
        if board[i][j] == 1:
            rect = True
            x = min(x, i)
            mx = max(mx, i)
            y = min(y, j)
            my = max(my, j)

if not rect:
    area = 0
else:
    area = (mx - x + 1) * (my - y + 1)

print(area)