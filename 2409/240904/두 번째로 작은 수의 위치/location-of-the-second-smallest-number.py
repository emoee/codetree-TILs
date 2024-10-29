n = int(input())
numbers = list(map(int, input().split()))

result = numbers.copy()
result.sort()

num = result[0]

position = 0
for i in range(1, n):
    if num < result[i]:
        num = result[i]
        if (i+1) < n and num == result[i+1]:
            position = -1
        break
    
    if i == (n-1) and num == result[i]:
        position = -1
    

if position != -1:
    for i in range(n):
        if num == numbers[i]:
            position = i+1
            break

print(position)