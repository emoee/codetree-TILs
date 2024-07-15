n = int(input())
cows = (list(map(int, input().split())))

count = 0
for i in range(n-2):
    if (cows[i] <= cows[i+1] <= cows[i+1]):
        count += 1
print(count)