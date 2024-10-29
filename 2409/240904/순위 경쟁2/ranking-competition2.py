n = int(input())

score = [
    tuple(map(str, input().split()))
    for _ in range(n)
]

top = 0
A, B = 0, 0
current = 3
for c, s in score:
    if c == 'A':
        A += int(s)
    else:
        B += int(s)
    
    currentTop = 0
    if A == B:
        currentTop = 3
    elif max(A, B) == A:
        currentTop = 1
    elif max(A, B) == B:
        currentTop = 2

    if current == currentTop:
        continue
    else:
        top += 1
        current = currentTop

print(top)