from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[0]*n for _ in range(n)]

def inrange(x, y):
    return 0 <= x < n and 0 <= y < n

def push(x, y, v):
    board[x][y] = v
    queue.append((x, y))

queue = deque()
push(r1-1, c1-1, 0)
answer = -1

def bfs():
    global answer
    dxs, dys = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2 , 2, -2, 2, -1, 1]
    while queue:
        x, y = queue.popleft()

        if x == r2-1 and y == c2-1:
            answer = board[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if inrange(nx, ny):
                push(nx, ny, board[x][y]+1)

bfs()
print(answer)