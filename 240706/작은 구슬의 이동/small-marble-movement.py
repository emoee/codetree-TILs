n, t = map(int, input().split())
r, c, d = map(str, input().split())

mappper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3,
}

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
x, y = int(r), int(c)
x -= 1
y -= 1
move = mappper[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(t):
    nx, ny = x+dxs[move], y+dys[move]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move = 3 - move

print(x+1, y+1)