n, b = map(int, input().split())

A = []
while True:
    if n < b:
        A.append(n)
        break
    
    A.append(n%b)
    n //= b

for a in A[::-1]:
    print(a, end="")