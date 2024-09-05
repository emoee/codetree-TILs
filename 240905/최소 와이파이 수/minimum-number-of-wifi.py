n, m = map(int, input().split())
wifi = list(map(int, input().split()))

mid = m//2

count = 0
for i in range(mid, n-mid, m):
    num = 0
    for j in range(i-mid, (i+mid+1)):
        if wifi[j] == 1:
            num += 1
    
    if num > 0:
        count += 1

print(count)