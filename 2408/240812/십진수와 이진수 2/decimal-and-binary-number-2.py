A = input()
n = 0

for i in range(len(A)):
    n = n*2 + int(A[i])

n *= 17
A = []
while True:
    if n < 2:
        A.append(n)
        break
    
    A.append(n%2)
    n //= 2

for a in A[::-1]:
    print(a, end="")