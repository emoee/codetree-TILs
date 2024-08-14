n, m = map(int, input().split())

A = []
B = []

a, b = 0, 0
for i in range(n):
    v, t = map(int, input().split())

    for j in range(t):
        a += v
        A.append(a)
    

for i in range(m):
    v, t = map(int, input().split())

    for j in range(t):
        b += v
        B.append(b)

result = 0
pre = None

for i in range(len(A)):
    if A[i] > B[i]:
        now = 'A'
    elif A[i] < B[i]:
        now = 'B'
    
    if A[i] == B[i] or (now != pre and pre != ''):
        result += 1 
    pre = now 


print(result-1)