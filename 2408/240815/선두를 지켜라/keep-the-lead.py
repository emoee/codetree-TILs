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
pre = ''

u = min(len(A), len(B))
for i in range(u):
    if A[i] > B[i]:
        now = 'A'
    elif A[i] < B[i]:
        now = 'B'
    else:
        now = pre
    
    if now != pre and pre != '':
        result += 1 
    
    pre = now 

print(result)