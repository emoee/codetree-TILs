n = int(input())

numbers = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

MAXV = 11

count = 0
for i in range(MAXV):
    for j in range(MAXV):
        for k in range(MAXV):
            success = True
            for x, y in numbers:
                if x == i or x == j or x == k:
                    continue
                
                success = False
            if success:
                count = 1
            
            success = True
            for x, y in numbers:
                if y == i or y == j or y == k:
                    continue
                
                success = False
            if success:
                count = 1

            success = True
            for x, y in numbers:
                if x == i or x == j or y == k:
                    continue
                
                success = False
            if success:
                count = 1

            success = True
            for x, y in numbers:
                if x == i or y == j or y == k:
                    continue
                
                success = False
            if success:
                count = 1

print(count)