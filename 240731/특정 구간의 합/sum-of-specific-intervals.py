n, m = map(int, input().split())
A = list(map(int, input().split()))

def f(A , a, b):
    s = 0
    for i in range(a, b+1):
        s += A[i-1]
    return s

for i in range(m):
    a, b = map(int, input().split())
    s = f(A , a, b)
    print(s)