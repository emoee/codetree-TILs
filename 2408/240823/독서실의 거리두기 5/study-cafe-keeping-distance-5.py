n = int(input())
seat = list(input())

value = 0
for i in range(n):
    if seat[i] != '1':
        seat[i] = '1'

        count = 0
        for j in range(i+1, n):
            if seat[j] == '0':
                count += 1
            else:
                break
        value = max(count, value)
        seat[i] = '0'
    else:
        continue

print(value)