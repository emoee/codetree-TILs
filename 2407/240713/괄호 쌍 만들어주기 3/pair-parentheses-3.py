listA = (list(input()))

count = 0
for i in range(len(listA)):
    if listA[i] == "(":
        for j in range(i, len(listA)):
            if listA[j] == ")":
                count += 1

print(count)