n, m = map(int, input().split())
A = list(map(int, input().split()))

def f(A, m):
    s = 0
    while(m >= 1):
        s += A[m-1]
        if m%2 == 0:
            m //= 2
        else:
            m -= 1
        
    return s

print(f(A, m))