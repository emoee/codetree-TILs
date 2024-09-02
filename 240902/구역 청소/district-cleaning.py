a, b = map(int, input().split())
c, d = map(int, input().split())

x = min(a, c)
y = max(b, d)

print(abs(x-y))