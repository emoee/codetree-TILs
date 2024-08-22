n = int(input())

numbers = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
MAV = 101

result = MAV

for x in range(0, MAV, 2):
    for y in range(0, MAV, 2):
        p1, p2, p3, p4 = 0, 0, 0, 0
        for n, m in numbers:
            if n > x and m > y:
                p1 += 1
            elif n < x and m < y:
                p2 += 1
            elif n > x and m < y:
                p3 += 1
            elif n < x and m > y:
                p4 += 1
        
        value = max(p1, p2, p3, p4)
        result = min(value, result)

print(result)