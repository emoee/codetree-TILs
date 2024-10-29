n = int(input())

heights = [
    int(input()) for _ in range(n)
]

cost = 10000 * 10000

for low in range(0, 84):
    high = low + 17
    value = 0

    for height in heights:
        if height > high:
            value += (height-high) ** 2
        elif height < low:
            value += (low-height) ** 2

    cost = min(cost, value)
    
print(cost)