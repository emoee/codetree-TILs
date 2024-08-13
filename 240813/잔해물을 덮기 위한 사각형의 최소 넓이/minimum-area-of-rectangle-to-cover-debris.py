board = [[0]*2000 for _ in range(2000)]

x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000
for j in range(x1, x2):
    for k in range(y1, y2):
        board[j][k] = 1


x1, y1, x2, y2 = map(int, input().split())
x1, y1, x2, y2 = x1+1000, y1+1000, x2+1000, y2+1000
for j in range(x1, x2):
    for k in range(y1, y2):
        board[j][k] = 0

area = sum(sum(row) for row in board)
print(area)