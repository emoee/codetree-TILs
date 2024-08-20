def check(heights, number):
    count = 0
    T = False

    for h in heights:
        if h > number:
            if not T:
                count += 1
                T = True
        else:
            T = False
    
    return count


n = int(input())
heights = [int(input()) for _ in range(n)]

MAXH = max(heights)
result = 0

for i in range(MAXH + 1):
    value = check(heights, i)
    result = max(result, value)

print(result)