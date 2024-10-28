n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(i, j, std):
    count = 1
    stack = [(i, j)]
    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]

    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+x, dy+y
            if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] == std:
                visited[nx][ny] = True
                count += 1
                stack.append((nx,ny))
    return count

block, maxBlock = 0, 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            result = dfs(i, j, board[i][j])
            
            maxBlock = max(result, maxBlock)
            if result >= 4:
                block += 1
                
print(block, maxBlock)