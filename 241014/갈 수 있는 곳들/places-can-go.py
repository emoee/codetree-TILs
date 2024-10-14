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
    global road
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == n-1:
            return True

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if inrange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 1:
                visited[nx][ny] = True
                board[nx][ny] = road
                road += 1
                queue.append((nx,ny))

answer = 0
for i in range(k):
    x, y = map(int, input().split())
    road = 0
    queue = deque()
    queue.append((x-1, y-1))

    bfs()
    answer += road

print(answer)