n, m = map(int, input().split())

Anumbers = list(map(int, input().split()))
Bnumbers = list(map(int, input().split()))

count = 0
for i in range(n-m+1):
    check = [0] * m
    for j in range(i, i+m):
        for k in range(m):
            if check[k] == 0 and Anumbers[j] == Bnumbers[k]:
                check[k] = 1
                break

    if sum(check) == m:
    #     print(i, Anumbers[i], check)
        count+=1

print(count)