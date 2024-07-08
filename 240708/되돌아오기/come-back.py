n = int(input())

dxs, dys = [1, 0, 0, -1],[0, 1, -1, 0]
mapper = {
    'N' : 0,
    'E' : 1,
    'W' : 2,
    'S' : 3
}
x, y = 0, 0
time = 0
for i in range(n):
    word, count = map(str, input().split())
    move = mapper[word]
    for j in range(int(count)):
        time += 1
        if word == 'N' or word == 'S':
            x, y = x+dxs[move], y+dys[move]
        else:
            x, y = x+dxs[move], y+dys[move]

        if x == 0 and y == 0:
            print(time)
            break

 if x != 0 and y != 0:
    print(-1)