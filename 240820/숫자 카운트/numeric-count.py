n = int(input())

order = []
for i in range(n):
    number, s, b = map(int, input().split())
    order.append((number, s, b))

count = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or j == k or i == k:
                continue
            
            success = True
            for n, s, b in order:
                x = n//100
                y = n//10 % 10
                z = n % 10

                S, B = 0, 0

                if i == x:
                    S += 1
                if j == y:
                    S += 1
                if k == z:
                    S += 1
                if x == j or x == k:
                    B += 1
                if y == i or y == k:
                    B += 1
                if z == i or z == j:
                    B += 1

                if S != s or B != b:
                    success = False
                    break
            if success:
                count += 1

print(count)