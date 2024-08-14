n, m = map(int, input().split())

A = []
B = []

a, b = 1000000, 1000000
for i in range(n):
    t, d = map(str, input().split())
    t = int(t)

    if d == "R":
        for j in range(t):
            a += 1
            A.append(a)
    else:
        for j in range(t):
            a -= 1
            A.append(a)
            
for i in range(m):
    t, d = map(str, input().split())
    t = int(t)

    if d == "R":
        for j in range(t):
            b += 1
            B.append(b)
    else:
        for j in range(t):
            b -= 1
            B.append(b)

result = 0
if len(A) > len(B):
    B.extend([B[-1]] * (len(A)-len(B)))
elif len(A) < len(B):
    A.extend([A[-1]] * (len(B)-len(A)))

for i in range(1, len(A)):
    if A[i] == B[i] and A[i-1] != B[i-1]:
        result += 1

print(result)