n, m = map(int, input().split())
wifi = list(map(int, input().split()))

count = 0
position = 0
while position < n:
    if wifi[position] == 1:
        count += 1
        position += 2 * m + 1
    else:
        position += 1

print(count)