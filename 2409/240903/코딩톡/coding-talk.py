person, message, number = map(int, input().split())

talk = [
    tuple(map(str, input().split()))
    for _ in range(message)
]
check = [0] * 27
for i in range(number-1, 101):
    if i < message:
        c, u = talk[i]
        check[ord(c)-65] = 1
    else:
        break

before = int(talk[number-1][1])
for i in reversed(range(number)):
    c, u = talk[i]
    if before == int(u):
        c2, u2 = talk[i]
        check[ord(c2)-65] = 1
    else:
        break

answer = [""] * 27
U = talk[number-1][1]
U = int(U)

if U > 0:
    for i in range(person):
        if check[i] != 1:
            answer[i] = chr(i+65)

for i in range(27):
    if answer[i] != "":
        print(answer[i], end=" ")