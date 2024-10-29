n = int(input())

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

board = [0] * n

for i in range(n):
    board[i] = list(map(int, input().split()))

result = 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i+dx, j+dy
            if in_range(nx, ny) and board[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            result += 1
        cnt = 0

print(result)