a, b, c = map(int, input().split())

result, value = 0, 0

aa, bb = c//a+1, c//b+1
for i in range(aa): #
    for j in range(bb):
        value += (a*i) + (b*j)
        
        if value <= c:
            result = max(result, value)
        value = 0

print(result)