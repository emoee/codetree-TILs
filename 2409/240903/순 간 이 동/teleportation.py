a, b, x, y = map(int, input().split())

count = min(abs(b-a), abs(x-a)+abs(b-y), abs(y-a)+abs(b-x))
print(count)