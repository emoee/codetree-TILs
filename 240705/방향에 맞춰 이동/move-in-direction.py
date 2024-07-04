n = int(input())
nx, ny = 0, 0

for i in range(n):
    d, k = map(str, input().split())
    if d == "N":
        ny = ny+int(k)
    elif d == "E":
        nx = nx+int(k)
    elif d == "S":
        ny = ny-int(k)
    elif d == "W":
        nx = nx-int(k)

print(nx, ny)