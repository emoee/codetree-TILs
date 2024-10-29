n = int(input())

numbers = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(i, n):
        sumValue = 0
        for k in range(i, j+1):
            sumValue += numbers[k]
        
        T = sumValue/(j+1-i)
        
        for k in range(i, j+1):
            if numbers[k] == T:
                count += 1
                break

print(count)