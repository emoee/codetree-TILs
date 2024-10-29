test = list(input())
x, y = [1, 0, -1, 0], [0, -1, 0, 1] # 좌, 하, 우, 상
dx, dy = 0, 0
dir_number = 3
for i in range(len(test)):
    if test[i] == "L":
        dir_number = (dir_number+3)%4
    elif test[i] == "R":
        dir_number = (dir_number+1)%4
    elif test[i] == "F":
        dx, dy = dx+x[dir_number], dy+y[dir_number]

print(dx, dy)