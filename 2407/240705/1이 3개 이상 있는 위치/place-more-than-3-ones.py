n = int(input())
result = [[0]*n for _ in range(n)]

for i in range(n):
    result[i] = (list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

count = 0
check = 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
for i in range(n):
    for j in range(n):
        check = 0
        for dx, dy in zip(dxs, dys):
            ci, cj = i+dx, j+dy
            if in_range(ci, cj) and result[ci][cj] == 1:
                check += 1
        if check > 2:
            count +=1   

print(count)