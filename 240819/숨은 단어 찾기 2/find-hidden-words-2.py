n, m = map(int, input().split())

board= [[0]*m for _ in range(n)]

for i in range(n):
    board[i] = list(input())

def right(x, y):
    return board[x][y] == 'L' and board[x][y+1] == 'E' and board[x][y+2] == 'E'

def left(x, y):
    return board[x][y] == 'L' and board[x][y-1] == 'E' and board[x][y-2] == 'E'

def top(x, y):
    return board[x][y] == 'L' and board[x-1][y] == 'E' and board[x-2][y] == 'E'

def bottom(x, y):
    return board[x][y] == 'L' and board[x+1][y] == 'E' and board[x+2][y] == 'E'

def diagonal(x, y):
    if in_range(x+2, y+2) and board[x][y] == 'L' and board[x+1][y+1] == 'E' and board[x+2][y+2] == 'E':
        return True
    elif in_range(x-2, y-2) and board[x][y] == 'L' and board[x-1][y-1] == 'E' and board[x-2][y-2] == 'E':
        return True
    elif in_range(x+2, y-2) and board[x][y] == 'L' and board[x+1][y-1] == 'E' and board[x+2][y-2] == 'E':
        return True  
    elif in_range(x-2, y+2) and board[x][y] == 'L' and board[x-1][y+1] == 'E' and board[x-2][y+2] == 'E':
        return True
    else:
        return False


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

count = 0

for x in range(n):
    for y in range(m):
        if in_range(x, y+2) and right(x, y):
            count += 1
        if in_range(x, y-2) and left(x, y):
            count += 1
        if in_range(x-2, y) and top(x, y):
            count += 1
        if in_range(x+2, y) and bottom(x, y):
            count += 1
        if diagonal(x, y):
            count += 1

print(count)