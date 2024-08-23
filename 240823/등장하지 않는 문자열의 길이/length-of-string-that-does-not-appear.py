n = int(input())
text = list(input())
result = [0] * n

for i in range(n):
    value = chr(ord(text[i])+1)
    count = 1
    for j in range(i+1, n):
        if value == text[j]:
            count += 1
            value = chr(ord(text[j])+1)
        else:
            break
    
    result[i] = count

result.sort()

if result[-1] == result[-2]:
    print(result[-3])
else:
    print(result[-1])