def f(a, b):
    minN = min(a, b)
    if minN == a:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2
    return a, b

n, m = map(int, input().split())
n, m = f(n, m)
print(n, m)