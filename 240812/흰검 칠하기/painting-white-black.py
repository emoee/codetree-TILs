n = int(input())
MAX_K = 100000
Rline = [0] * (2 * MAX_K + 1)
Lline = [0] * (2 * MAX_K + 1)
line = [0] * (2 * MAX_K + 1)

now = MAX_K
for i in range(n):
    x, c = map(str, input().split())
    x = int(x)

    if c == "L":
        for j in range(x):
            now -= 1
            line[now] = 1
            Lline[now] += 1
    else:
        for j in range(x):
            line[now] = 2
            Rline[now] += 1
            now += 1

gray, white, black = 0, 0, 0
for k in range(2 * MAX_K + 1):
    if Rline[k] >= 2 and Lline[k] >= 2:
        gray += 1
    elif line[k] == 1:
        white += 1
    elif line[k] == 2:
        black += 1

print(white, black, gray)