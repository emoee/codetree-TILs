n, m = map(int, input().split())

Anumbers = list(map(int, input().split()))
Bnumbers = list(map(int, input().split()))

count = 0
for i in range(n-m+1):
    check = [0] * m
    for j in range(i, i+m):
        for k in range(m):
            if Anumbers[j] == Bnumbers[k]:
                check[k] = 1
    if sum(check) == m:
        count+=1

print(count)