n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

birds = [0] * 11

lines.sort()
start = lines[0][0]
birds[start] = lines[0][1]
for i in range(1, n):
    if start == lines[i][0]:
        continue
    
    birds[lines[i][0]] = lines[i][1]
    start = lines[i][0]

count = 0

for bird, position in lines:
    if birds[bird] != position:
        birds[bird] = position
        count += 1

print(count)