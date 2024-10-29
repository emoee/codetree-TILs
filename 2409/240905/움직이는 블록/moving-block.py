n = int(input())
numbers = [
    int(input()) for _ in range(n)
]

mid = sum(numbers)//n

count = 0
for i in range(n):
    if numbers[i] > mid:
        count += numbers[i]-mid
    
print(count)