n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def inrange(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(visited, i, j, mid):
    stack = [(i, j)]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] > mid:
                visited[nx][ny] = True
                stack.append((nx, ny))

def findArea(mid):
    count = 0
    visited = [[False]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if inrange(i, j) and not visited[i][j] and board[i][j] > mid:
                count += 1
                visited[i][j] = True
                dfs(visited, i, j, mid)

    return count

maxValue = max(map(max, board))+1
k, answer = 100, 0

for i in range(1, maxValue):
    result = findArea(i)
    if result > answer:
        k, answer = i, result
    elif result == answer:
        k = i

print(k, answer)