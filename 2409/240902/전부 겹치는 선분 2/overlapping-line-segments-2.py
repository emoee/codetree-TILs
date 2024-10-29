n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

answer = "No"
for i in range(n):
    q, p = lines[i]
    
    x, y = lines[(i+1)%n]
    check = True
    for a, b in lines:
        if q == a and p == b:
            continue
        if a > y or b < x:
            check = False
            break
        else:
            x = max(x, a)
            y = min(y, b)
    
    if check:
        answer = "Yes"

print(answer)