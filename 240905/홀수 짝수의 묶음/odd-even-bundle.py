n = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

count = 0

while True:
    if count % 2 == 0:
        if even:
            even -= 1
            count += 1
        elif odd >= 2:
            odd -= 2
            count += 1
        else:
            if even > 0 or odd > 0:
                count -= 1
        
            break
    else:
        if odd:
            odd -= 1
            count += 1
        else:
            break

print(count)