n, m = map(int, input().split())

array = [
    tuple(map(int, input().split()))
    for _ in range(m)
]

result = 0
for i in range(m):
    count = 0 
    x, y = array[i]
    for a, b in array:
        if (x == a or y == a) and (x == b or y == b):
            count += 1
        
    result = max(result, count)

print(result)