digits = input()

n = 0
for i in range(len(digits)):
    n = n*2 + int(digits[i])

print(n)