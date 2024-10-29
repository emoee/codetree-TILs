# a = int(input())

# print(int(str(a), 2))

strA = list(map(int, list(input())))

maxValue = 0
for i in range(1, len(strA)):
    strA[i] = 1 - strA[i]

    num = 0
    for j in range(len(strA)):
        num = num * 2 + strA[j]
    
    maxValue = max(maxValue, num)

    strA[i] = 1 - strA[i]

print(maxValue)