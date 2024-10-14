from collections import deque

n, k = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[False]*n for _ in range(n)]
def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs():
    while queue:
        x, y = queue.popleft()
        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 1:    
                visited[nx][ny] = True
                queue.append((nx,ny))

queue = deque()
for i in range(k):
    x, y = map(int, input().split())
    queue.append((x-1, y-1))
    visited[x-1][y-1] = True

bfs()
answer = sum(v.count(True) for v in visited)
print(answer)