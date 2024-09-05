n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result = 1000000000

for i in range((2*n-n)):
    # print(numbers[n+i]-numbers[i])
    result = min(result, numbers[n+i]-numbers[i])

print(result)