n = int(input())

board = [[0]*n for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

dxs, dys = [0, 0, 0], [0, 1, 2]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

maxValue = 0
for x in range(n):
    for y in range(n-2):
        for i in range(n):
            for j in range(n-2):
                if x == i and abs(y-j) <= 2:
                    continue
                count1, count2 = 0, 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    if in_range(nx, ny):
                        count1 += board[nx][ny]
                for dx, dy in zip(dxs, dys):
                    nx, ny = i+dx, j+dy
                    if in_range(nx, ny):
                        count2 += board[nx][ny]
                maxValue = max(maxValue, count1 + count2)
    

print(maxValue)