n, b = map(int, input().split())

order = [
    list(map(int, input().split()))
    for _ in range(n)
]

result = 0
for i in range(n):
    test = []
    total = 0

    for k in range(n):
        if i == k:
            test.append(order[k][0]/2 + order[k][1])
        else:    
            test.append(sum(order[k]))
    
    test.sort()
    
    for j in range(n):
        price = test[j]
        if total + price <= b:
            total += price
        else:
            result = max(result, j)
            break
    
        
print(result)