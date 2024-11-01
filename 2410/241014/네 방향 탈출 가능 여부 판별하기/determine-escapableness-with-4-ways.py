from collections import deque

n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*m for _ in range(n)]
def inrange(x, y):
    return 0 <= x < n and 0 <= y < m
road = 0
queue = deque()
queue.append((0, 0))
def bfs():
    global road
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            return True

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = True
                board[nx][ny] = road
                road += 1
                queue.append((nx,ny))

if bfs():
    print(1)
else:
    print(0)