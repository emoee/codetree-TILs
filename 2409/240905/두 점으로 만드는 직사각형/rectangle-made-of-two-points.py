x, y, x2, y2 = map(int, input().split())
a, b, a2, b2 = map(int, input().split())

ax = min(x, a)
ax2 = max(x2, a2)
by = min(y, b)
by2 = max(y2, b2)

result = abs(ax2-ax) * abs(by2-by)
print(result)