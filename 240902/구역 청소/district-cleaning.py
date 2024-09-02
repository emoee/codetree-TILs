a, b = map(int, input().split())
c, d = map(int, input().split())

if c < a or b > d:
    x = min(a, c)
    y = max(b, d)

    print(abs(x-y))
else:
    print((b-a) + (d-c))