n , m = map(int, input().split())

def f(a, b):
    s = 1
    for i in range(2, min(a,b)):
        if a%i == 0 and b%i == 0:
            s *= i
    
    return s

print(f(n, m))