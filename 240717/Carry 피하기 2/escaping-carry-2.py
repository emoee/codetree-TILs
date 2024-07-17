def number(t):
    return list(map(int, str(t)))

def sameLen(x, y, z):
    maxLen = max(len(x), len(y), len(z))
    x = [0] * (maxLen - len(x)) + x
    y = [0] * (maxLen - len(y)) + y
    z = [0] * (maxLen - len(z)) + z
    return x, y, z

n = int(input())
A = []

for i in range(n):
    A.append(int(input()))


maxValue = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            x = number(A[i])
            y = number(A[j])
            z = number(A[k])

            x, y, z = sameLen(x,y,z)
            check = True
            
            while x and y and z:
                if x.pop() + y.pop() + z.pop() > 9:
                    check = False
                    break
            
            if check == True and A[i]+A[j]+A[k] > maxValue:
                maxValue = A[i]+A[j]+A[k]

print(maxValue)