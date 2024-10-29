n, m, k = map(int, input().split())

student = []
check = [k] * (n+1)
for i in range(m):
    student.append(int(input()))

result = -1
for s in student:
    check[s] -= 1
    if check[s] == 0:
        result = s
        break

print(result)