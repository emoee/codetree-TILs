n = int(input())

board = [[0]*n for _ in range(n)]
result = []

for i in range(n):
    board[i] = list(map(int, input().split()))

dxs, dys = [0, 0, 0], [0, 1, 2]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for x in range(n):
    for y in range(0, n, 2):
        count = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                count += board[nx][ny]
        result.append(count)
    

result.sort()
print(result[-1] + result[-2])