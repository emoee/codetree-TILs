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

answer = ""
for i in range(person):
    if check[i] != 1:
        answer += chr(i+65) + " "

print(answer)