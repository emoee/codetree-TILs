n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

birds = [2] * 11

for i in range(n):
    bird, position = lines[i]
    if birds[bird] == 2:
        birds[bird] = position

count = 0

for bird, position in lines:
    if birds[bird] != position:
        birds[bird] = position
        count += 1

print(count)