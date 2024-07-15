a = int(input())

# print(int(str(a), 2))

strA = list(str(a))

maxValue = int(str(a), 2)
for i in range(1, len(strA)):
    strA[i] = str(1 - int(strA[i]))
    if int(''.join(strA)) > maxValue:
        maxValue = int(''.join(strA))

print(int(str(maxValue), 2))