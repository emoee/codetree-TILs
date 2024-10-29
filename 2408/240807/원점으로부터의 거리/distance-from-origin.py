n = int(input())
board = []
for i in range(n):
    x, y = map(int, input().split())
    m = abs(0-x) + abs(0-y)
    board.append((i+1,x,y,m))

board.sort(key=lambda x: x[3])

for b in board:
    print(b[0])