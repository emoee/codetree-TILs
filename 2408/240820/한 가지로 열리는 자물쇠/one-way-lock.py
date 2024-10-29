def lock(x, y, z):
    return(abs(a-x) > 2 and abs(b-y) > 2 and abs(c-z) > 2)

n = int(input())

a, b, c = map(int, input().split())
result = n*n*n
count = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if lock(i, j, k):
                count += 1
            
    
print(result - count)