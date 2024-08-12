a, b = map(int, input().split())
n = input()

c = 0
for i in range(len(n)):
    c = c*a + int(n[i])

result = []
while True:
    if c < b:
        result.append(c)
        break
    result.append(c%b)
    c //= b

for r in result[::-1]:
    print(r, end="")