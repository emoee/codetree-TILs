moves = (list(input()))

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0], 
time = 0
t = 0

x, y = 0, 0 
for index, move in enumerate(moves):
    x, y = x+dxs[t], y+dys[t]
    if move == 'L':
        t = t + 1 % 4
    elif move == 'R':
        t = t + 1 % 4
    if x == 0 and y == 0:
        print(time)
        break
    
    time += 1
    if len(moves)-1 == index:
        print(-1)