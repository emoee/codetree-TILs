n, b = map(int, input().split())

order = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

result = 0
for i in range(n):
    total = (order[i][0]/2) + order[i][1]
    for j in range(n):
        price = sum(order[j])
        if total + price <= b:
            total += price
        else:
            result = max(result, j)

print(result)