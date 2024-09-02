n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

x, y = lines[0]
answer = "Yes"
for a, b in lines:
    if a > y or b < x:
        answer = "No"
        break
    else:
        x = max(x, a)
        y = min(y, b)

print(answer)