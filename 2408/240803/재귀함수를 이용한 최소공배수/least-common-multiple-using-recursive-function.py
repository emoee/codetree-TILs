n = int(input())
s = list(map(int, input().split()))

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

def lcm(x, y):
    return abs(x*y) // gcd(x, y)

result = 1
for i in s:
    result = lcm(result, i)

print(result)