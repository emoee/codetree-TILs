n = int(input())

result = []

for i in range(1, int(n**(1/2)) + 1):
    if (n%i) == 0:
        result.append(i)
        if ( (i**2) != n) : 
            result.append(n // i)
            
result.sort()
print(" ".join(map(str,result)))