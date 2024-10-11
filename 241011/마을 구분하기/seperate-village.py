n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count = 0

def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global count
    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = dx+x, dy+y
        if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == 1:
            visited[nx][ny] = True
            count += 1
            dfs(nx, ny)

answer = []
for i in range(n):
    for j in range(n):
        count = 0
        if board[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            answer.append(count)

answer.sort()
print(len(answer))
for i in answer:
    print(i)