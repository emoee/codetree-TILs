n = int(input())

numbers = list(map(int, input().split()))

result = sum(numbers)
for i in range(n):
    numbers[i] *=2
    
    for j in range(n):
        remaining = [elem for m, elem in enumerate(numbers) if m != j]
        
        sumValue = 0
        for k in range(n-2):
            sumValue += abs(remaining[k] - remaining[k+1])

        result = min(result, sumValue)
    
    numbers[i] //= 2
    

print(result)