n = int(input())

board = [[0]*n for _ in range(n)]
result = [0] * n

for i in range(n):
    board[i] = list(map(int, input().split()))

dxs, dys = [0, 0, 0], [0, 1, 2]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for x in range(n):
    maxValue = 0
    for y in range(n):
        count = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                count += board[nx][ny]
        maxValue = max(maxValue, count)
    result[x] = maxValue

result.sort()
print(result[-1] + result[-2])