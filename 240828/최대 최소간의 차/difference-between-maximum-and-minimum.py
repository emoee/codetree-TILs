n, k = map(int, input().split())
numbers = list(map(int, input().split()))

result = 10000 * 10000
for l in range(99):
    h = l + 2
    cost = 0

    for n in numbers:
        if n > h:
            cost += abs(n-h)
        elif n < l:
            cost += abs(l-n)
    
    result = min(cost, result)

print(result)