n, b = map(int, input().split())

order = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0
for i in range(n):
    test = sorted(order)
    test[i][0] = test[i][0]//2
    total = sum(test[i])

    test.sort()
    for j in range(n):
        price = sum(test[j])
        if total + price <= b:
            total += price
        else:
            result = max(result, j)
            break
        
print(result)