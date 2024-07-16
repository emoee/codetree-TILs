A = list(input())

count = 0
check = 0
for i in range(len(A)-1):
    if A[i] == A[i+1] and A[i] == "(":
        for j in range(i, len(A)-1):
            if A[j] == A[j+1] and A[j] == ")":
                check += 1

print(check)