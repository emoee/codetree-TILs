n , m = map(int, input().split())

def f(a, b):
    s = 1
    a1, b1 = a, b
    for i in range(2, min(a,b)):
        if a%i == 0 and b%i == 0:
            s *= i
            a, b = a//i, b//i
    
    s *= (a1 // s) * (b1 // s)
    return s

print(f(n, m))