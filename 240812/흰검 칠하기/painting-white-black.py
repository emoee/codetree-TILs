n = int(input())

Rline = [0] * 200
Lline = [0] * 200
line = [""] * 200

now = 100
for i in range(n):
    x, c = map(str, input().split())
    x = int(x)
    if c == "L":
        while x > 0:
            line[now] = 'w'
            Lline[now] += 1
            x -= 1
            if x:
                now -= 1
    else:
         while x > 0:
            line[now] = 'b'
            Rline[now] += 1
            x -= 1
            if x:
                now += 1

gray, white, black = 0, 0, 0
for k in range(200):
    if Rline[k] >= 2 and Lline[k] >= 2:
        gray += 1
    elif line[k] == 'w':
        white += 1
    elif line[k] == 'b':
        black += 1

print(white, black, gray)