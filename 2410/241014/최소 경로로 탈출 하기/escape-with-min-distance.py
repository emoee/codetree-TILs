from collections import deque

n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*m for _ in range(n)]

def inrange(x, y):
    return 0 <= x < n and 0 <= y < m

def push(x, y, v):
    board[x][y] = v
    visited[x][y] = True
    queue.append((x, y))

queue = deque()
push(0, 0, 0)

def bfs():
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 0:
                push(nx, ny, board[x][y]+1)

bfs()
answer = board[n-1][m-1]
if answer > 1:
    print(answer)
else:
    print(-1)