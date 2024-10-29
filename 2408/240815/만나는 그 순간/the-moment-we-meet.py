MAXT = 1000000

n, m = map(int, input().split())

A = [0] * (MAXT + 1)
B = [0] * (MAXT + 1)

a, b = 1, 1

for i in range(n):
    d, t = map(str, input().split())
    t = int(t)

    if d == "R": 
        for j in range(t):
            A[a] = A[a-1] + 1
            a += 1
    else:
        for j in range(t):
            A[a] = A[a-1] - 1
            a += 1

for i in range(m):
    d, t = map(str, input().split())
    t = int(t)

    if d == "R": 
        for j in range(t):
            B[b] = B[b-1] + 1
            b += 1
    else:
        for j in range(t):
            B[b] = B[b-1] - 1
            b += 1

result = -1
for i in range(1, a):
    if A[i] == B[i]:
        result = i
        break

print(result)