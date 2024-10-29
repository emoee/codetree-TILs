n = int(input())

MAX_K = 100000
line = [''] * (2 * MAX_K + 1)

now = MAX_K
for i in range(n):
    x, c = map(str, input().split())
    x = int(x)
    if c == "R":
        for j in range(x):
            line[now] = 'b'
            if j < x-1:
                now += 1
    else:
        for j in range(x):
            line[now] = 'w'
            if j < x-1:
                now -= 1

w, b = 0, 0
for i in range(2 * MAX_K + 1):
    if line[i] == 'w':
        w += 1
    elif line[i] == 'b':
        b += 1
print(w, b)