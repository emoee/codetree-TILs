n, s = map(int, input().split())

numbers = list(map(int, input().split()))
cha = s
for i in range(n-1):
    for j in range(1, n):
        sumNumbers = sum(numbers)
        sumNumbers -= (numbers[i] + numbers[j])
        
        ssn = abs(s-sumNumbers)
        cha = min(ssn, cha)

print(cha)