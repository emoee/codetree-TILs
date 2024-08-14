MAXT = 1000000

n, m = map(int, input().split())

A = [0] * (MAXT + 1)
B = [0] * (MAXT + 1)

a, b = 1, 1
for i in range(n):
    v, t = map(int, input().split())

    for j in range(t):
        A[a] = A[a-1] + v/t
        a += 1
    

for i in range(m):
    v, t = map(int, input().split())

    for j in range(t):
        B[b] = B[b-1] + v/t
        b += 1

result = 0
for i in range(2, len(A)):
    if A[i] == 0 and B[i] == 0:
        break
    elif A[i-1] > B[i-1] and A[i] > B[i]:
        continue
    elif A[i-1] < B[i-1] and A[i] < B[i]:
        continue
    else:
        result += 1

print(result)